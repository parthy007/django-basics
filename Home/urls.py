from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="contact"),
    path('logout', views.logout, name="logout"),
    path('login', views.login, name="login"),
]
