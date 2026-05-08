from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page,name="home_page"),
    path('login/', views.login_page,name="login_page"),
    path('signup/', views.signup_page,name="signup_page"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('add-monitor/', views.add_monitor,name="add-monitor"),
    path('logout/', views.user_logout,name="logout"),
]