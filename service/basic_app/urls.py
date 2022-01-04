from django.urls import path
from servise_app import views


urlpatterns = [
    path('', views.users, name='users'),
]
