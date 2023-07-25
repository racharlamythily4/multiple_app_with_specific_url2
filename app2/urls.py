from django.urls import path
from app2.views import *

app2_name="something"
urlpatterns=[
    path("three/",three,name="three"),
    path("four/",four,name="four"),
    path("string/",string,name='string')
]