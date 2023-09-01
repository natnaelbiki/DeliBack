from rest_framework import generics, permissions
from .serializers import ShopSerializer
from supplier.models import Shop
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

@csrf_exempt
def login(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)
		print(data['username'])
		user = authenticate(request, 
			username=data['username'], 
			password=data['password'])
		if user is None:
			return JsonResponse(
				{'error':'unable to login. check username and password'},
				status=400)
		else:
			try:
				token = Token.objects.get(user=user)
			except: # if token not in db, create a new one
				token = Token.objects.create(user=user)
				return JsonResponse({'token':str(token)}, status=201)


@csrf_exempt
def signup(request):
	if request.method == 'POST':
		try:
			data = JSONParser().parse(request)
			user = User.objects.create_user(username=data['username'], password=data['password'])
			user.save()
			token = Token.objects.create(user=user)
			return JsonResponse({'token':str(token)},status=201)
		except IntegrityError:
			return JsonResponse({'error':'username taken. choose another username'},
				status=400)

class UpdateDestroyShop(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ShopSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		user = self.request.user
		return Shop.objects.filter(user=user)

class CreateShop(generics.ListCreateAPIView):
	serializer_class = ShopSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		user = self.request.user
		return Shop.objects.filter(user=user).order_by('-name')

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)