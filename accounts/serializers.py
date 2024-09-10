from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class AccountSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required = True)
    first_name = serializers.CharField(required = True)
    last_name = serializers.CharField(required = True)
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True)
    confirm_password = serializers.CharField(required = True)

    class Meta:
        model = models.UserAccount
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',
            'account_type',
            'account_no',
            'birth_date',
            'gender',
            'account_balance',
            'country',
            'city',
            'postal_code',
            'street_address',
        )
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        account_type = self.validated_data['account_type']
        account_no = self.validated_data['account_no']
        birth_date = self.validated_data['birth_date']
        gender = self.validated_data['gender']
        account_balance = self.validated_data['account_balance']
        country = self.validated_data['country']
        city = self.validated_data['city']
        postal_code = self.validated_data['postal_code']
        street_address = self.validated_data['street_address']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password :
            raise serializers.ValidationError({'error':"password doesn't mactched"})
        
        if User.objects.filter(username = username).exists():
            raise serializers.ValidationError({"error":"this username is already exits"})
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({"error":"this email is already exits"})
        
        account = User(username=username,first_name=first_name,last_name=last_name,email=email)
        account.set_password(password)
        account.save()

        models.UserAccount.objects.create(
            user = account,
            account_type = account_type,
            account_no = account_no,
            birth_date = birth_date,
            gender = gender,
            account_balance = account_balance,
            country = country,
            city = city,
            postal_code = postal_code,
            street_address = street_address
            
        )
        return account

class GetAllaccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserAccount
        fields = '__all__'

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

class GetUserNameSerialzers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email']
