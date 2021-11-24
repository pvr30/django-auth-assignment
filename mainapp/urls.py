from os import name
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('login', views.userlogin, name="login"),
    path('logout', views.userlogout, name="logout"),
    path('edit/<int:id>', views.edituser, name="edit"),
    path('delete/<int:id>', views.deleteuser, name="delete"),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]