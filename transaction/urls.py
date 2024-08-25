from django.urls import path,include
from . import views


urlpatterns = [
    path("transactionHistory/",views.TransactionApiVeiw.as_view(),name="transactionHistory"),
    path('deposit/', views.DepositeMoneyApiView.as_view(), name='deposit-money'),
    path('withdraw/', views.WithdrawMoneyApiView.as_view(), name='withdraw-money'),
    path('transferBalance/', views.TransferMoneyApiView.as_view(), name='transfer-money'),
]