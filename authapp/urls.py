from django.urls import path

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('<int:pk>', authapp.BorshchUserDetailView.as_view(), name='BorshchUSer'),
]