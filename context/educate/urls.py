from django.urls import path
from . import views


app_name = 'educate'

urlpatterns = [
    path('', views.index, name='index'),
]