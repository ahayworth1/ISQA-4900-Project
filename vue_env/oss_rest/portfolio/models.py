from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import generics, permissions


class RegisterView(generics.CreateAPIView):
    serializer_class = 'your_app_name.serializers.UserSerializer'
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        from .models import Token
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=201)


class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(default=timezone.now)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} - Customer: {self.customer.name}"

    # def name(self):
    #     return self.customer.name


class Inventory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Token(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='auth_tokens', db_column='user_id')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'token'
        verbose_name_plural = 'tokens'

    def __str__(self):
        return self.key


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        from .models import Token
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})



