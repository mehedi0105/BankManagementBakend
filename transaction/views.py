from django.shortcuts import render
from . import serializers
from rest_framework.views import APIView
from . import models
from rest_framework.response import Response
from rest_framework import  status
from accounts import models as accounts
from accounts.serializers import AccountSerializers
from django.http import Http404
# Create your views here.
class TransactionApiVeiw(APIView):
    def get(self,request):
        transactions  = models.TransactionHistory.objects.all()
        serializer = serializers.TransactionSerializers(transactions, many = True)
        return Response(serializer.data)
    
    def post(self,request, format=None):
        serializer = serializers.TransactionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DepositeMoneyApiView(APIView):
    def post(self,request, format=None):
        amount = request.data.get('amount')
        try:
            user = self.request.user
            account = accounts.UserAccount._default_manager.get(user = user)
        except(accounts.UserAccount.DoesNotExist):
           return Response({"error": "User account does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        if amount is not None:
            account.account_balance += amount
            account.save(
            update_fields=[
                'account_balance'
            ])
            return Response({"success":"Deposite Success"},status=status.HTTP_200_OK)
        return Response({"error": "Amount is required."}, status=status.HTTP_400_BAD_REQUEST)
    
class WithdrawMoneyApiView(APIView):
    def post(self,request, format=None):
        amount = request.data.get('amount')
        try:
            user = self.request.user
            account = accounts.UserAccount._default_manager.get(user = user)
        except(accounts.UserAccount.DoesNotExist):
           return Response({"error": "User account does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        if amount is not None:
            account.account_balance -= amount
            account.save(
            update_fields=[
                'account_balance'
            ])
            return Response({"success":"Withdraw Money Success"},status=status.HTTP_200_OK)
        return Response({"error": "Amount is required."}, status=status.HTTP_400_BAD_REQUEST)
    
class TransferMoneyApiView(APIView):
    def post(self,request, format=None):
        account = request.data.get('account')
        amount = request.data.get('amount')
        try:
            user = self.request.user
            account = accounts.UserAccount._default_manager.get(account_no = account)
            tran_account = accounts.UserAccount._default_manager.get(user = user)
        except(accounts.UserAccount.DoesNotExist):
           return Response({"error": "User account does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        if amount is not None:
            account.account_balance += amount
            tran_account.account_balance -= amount
            account.save(
            update_fields=[
                'account_balance'
            ])
            tran_account.save(
            update_fields=[
                'account_balance'
            ])
            return Response({"success":"Transfer Money Success"},status=status.HTTP_200_OK)
        return Response({"error": "Amount is required."}, status=status.HTTP_400_BAD_REQUEST)


