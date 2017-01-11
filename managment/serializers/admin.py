from rest_framework import serializers
from django.contrib.auth import get_user_model  # If used custom user model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserModel
		write_only_fields = ('password',)
		read_only_fields = ('id', 'date_joined')
		fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'is_staff', 'date_joined')

	def create(self, validated_data):
		user = UserModel.objects.create(
			username=validated_data['username'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name'],
			email=validated_data['email'],
			is_staff=validated_data['is_staff']
		)
		user.set_password(validated_data['password'])
		user.save()
		return user

	def update(self, instance, validated_data):
		if hasattr(validated_data, 'password'):
			validated_data.pop('password')

		return super(UserSerializer, self).update(instance, validated_data)


class PasswordSerializer(serializers.Serializer):
	password = serializers.CharField(style={'type': 'password'}, required=False)
