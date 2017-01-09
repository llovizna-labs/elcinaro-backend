from rest_framework import viewsets, status
from django.contrib.auth import get_user_model  # If used custom user model
from rest_framework.decorators import detail_route
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from managment.serializers import admin
from managment.serializers.admin import PasswordSerializer

UserModel = get_user_model()


class StandardResultsSetPagination(PageNumberPagination):
	page_size = 100
	page_size_query_param = 'page_size'
	max_page_size = 1000


class UserViewSet(viewsets.ModelViewSet):
	queryset = UserModel.objects.all()
	serializer_class = admin.UserSerializer
	model = UserModel
	pagination_class = StandardResultsSetPagination
	#filter_backends = (OrderingFilter, SearchFilter)
	ordering_fields = ('identificacion', 'telefono', 'email', 'created', 'updated')


	@detail_route(methods=['post'])
	def set_password(self, request, pk=None):
		user = self.get_object()
		serializer = PasswordSerializer(data=request.data)
		if serializer.is_valid():
			user.set_password(serializer.data['password'])
			user.save()
			return Response({'status': 'password set'})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
