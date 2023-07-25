from django.urls import path
from app3.views import *

app3_name='something'
urlpatterns=[
    path('five/',five,name='five'),
    path('six/',six,name='six'),
    path('string/',string,name="string")
]