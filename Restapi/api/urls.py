from django.urls import path
from home.views import index

urlpatters =[
    path('index/',index,name='index')
]