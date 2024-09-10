from django.shortcuts import render,redirect
from .serializers import AccountSerializers, UserLoginSerializer, GetUserNameSerialzers,GetAllaccountsSerializer
from rest_framework import viewsets,status,generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from . import models
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout


# Create your views here.
class AccountRegisterApiView(APIView):
    serializer_class = AccountSerializers

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            user.save()

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"https://bankmanagementbakend.onrender.com/accounts/activate/{uid}/{token}/"
            name = f"Hello {user.first_name}"
            email_subject = "Verify Your Email Address - Complete Your Registration"
            email_body = render_to_string('./register_email.html',{'confirm_link':confirm_link, 'name':name})
            email = EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()        
        user = User._default_manager.get(pk = uid)
    except user.DoesNotExist():
                user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("http://127.0.0.1:5500/Frontend/login.html")
    else:
        return HttpResponse("Activation link is invalid!", status=status.HTTP_400_BAD_REQUEST)
    
class GetAllAccountApiView(APIView):
    def get(self, request):
        try:
            accounts = models.UserAccount.objects.all()
            serializer = GetAllaccountsSerializer(accounts, many= True)
            return Response(serializer.data)
        except models.UserAccount.DoesNotExist:
            return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)
        
class GetAllUserApiView(APIView):
    def get(self, request):
        try:
            user = User.objects.all()
            serializer = GetUserNameSerialzers(user, many= True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class UserLoginApiView(APIView):
     def post(self,request):
          serializer = UserLoginSerializer(data = request.data)
          if serializer.is_valid():
               username = serializer.validated_data['username']
               password = serializer.validated_data['password']
               user = authenticate(username = username, password = password)
               if user:
                    token,_ = Token.objects.get_or_create(user=user)
                    login(request,user)
                    return Response({'token':token.key, 'user_id':user.id})
               return Response({"error":"Invalid Creadantial"})
          return Response(serializer.data)

class UserLogOut(APIView):
     def get(self,request):
          request.user.auth_token.delete()
          logout(request)
          return redirect('login')



