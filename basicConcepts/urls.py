from django.urls import path
from . import views

urlpatterns = [
    path('',views.Welc, name='Welcome'),
    path('user',views.User, name='User')
]