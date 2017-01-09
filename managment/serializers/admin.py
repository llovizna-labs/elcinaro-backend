
from rest_framework import serializers
from django.contrib.auth import get_user_model  # If used custom user model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserModel
		write_only_fields = ('password',)
		read_only_fields = ('id',)
		fields = ('id', 'first_name', 'last_name', 'username', 'email', 'is_staff')

	def create(self, validated_data):
		user = UserModel.objects.create(username=validated_data['username'])
		user.set_password(validated_data['password'])
		user.save()
		return user

	def update(self, instance, validated_data):
		if hasattr(validated_data, 'password'):
			instance.set_password(validated_data['password'])

		return super(UserSerializer, self).update(instance, validated_data)


class PasswordSerializer(serializers.Serializer):
	password = serializers.CharField( style={'type': 'password'}, required=False)