from django.urls import path
from app1.views import *

app1_name="something"
urlpatterns=[
    path("one/",one,name="one"),
    path("two/",two,name="two"),
    path("string/",string,name="string")
]