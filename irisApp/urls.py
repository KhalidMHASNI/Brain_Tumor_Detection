from django.urls import path
from . import views

urlpatterns = [
    path('',views.predictor),
    path('result',views.formInfo ,name='result'),
]