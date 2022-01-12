from django.urls import path
from basic_app import views


urlpatterns = [
   path('', views.new_form, name='new_form'),
]
