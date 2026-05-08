from django.urls import path
from . import views

urlpatterns = [
    path('monitors/', views.list_monitors,name="list_monitors"),
]