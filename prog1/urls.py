# coding=utf-8
from django.urls import path
from prog1.views import *

urlpatterns = [
    path('', Index.as_view()),
    path('person/', PersonV.as_view()),
    path('about/', About.as_view()),
    path('temp/', Index1.as_view()),
]
