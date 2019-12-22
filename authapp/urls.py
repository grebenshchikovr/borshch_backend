from django.urls import path

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('register/', authapp.register, name='register'),
    path('login/', authapp.LogIn.as_view(), name='login'),
    path('logout/', authapp.LogOut.as_view(), name='logout'),
    path('<int:pk>', authapp.BorshchUserDetailView.as_view(), name='BorshchUser'),
]