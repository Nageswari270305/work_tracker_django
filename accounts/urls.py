from django.urls import path
from .views import Accounts

urlpatterns =[
    path('signIn/',Accounts.as_view()),
]