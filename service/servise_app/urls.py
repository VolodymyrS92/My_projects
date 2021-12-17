from django.urls import path
from service.servise_app import views


urlpatterns = [
    path('', views.index, name='index'),
]
