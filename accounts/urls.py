from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register(r'register',views.AccountRegisterApiView, basename="register")

urlpatterns = [
#  path('',include(router.urls)),
    path("register/",views.AccountRegisterApiView.as_view(),name="register"),
    path("activate/<uid64>/<token>/",views.activate, name = "activate"),
    path('GetAllUser/', views.GetAllUserApiView.as_view() , name='getAllUser'),
    path("login/",views.UserLoginApiView.as_view(), name = "login"),
    path("logout/",views.UserLogOut.as_view(), name = "logout"),
]