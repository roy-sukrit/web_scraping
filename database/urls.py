from django.contrib import admin
from django.urls import path
from database import views

urlpatterns = [
    path('', views.base, name="home"),
    path('page2', views.page2, name="page2"),
    path('page3', views.page3, name="page3"),
    path('page4', views.page4, name="page4"),
    path('page5', views.page5, name="page5"),
    path('page6', views.page6, name="page6"),
    path('page7', views.page7, name="page7"),
    path('page8', views.page8, name="page8"),
   
]
