from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[path('uploads/aerial/', uploadPage_aerial,name="uploadPage_aerial"),
path('uploads/semantic/',uploadPage_semantic,name="uploadPage_semantic"),
path('uploads/sketch/',uploadPage_sketch,name="uploadPage_sketch"),
path('uploads/display/',display_output,name='display_output'),
]