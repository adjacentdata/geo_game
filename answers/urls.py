from django.urls import path, include
from django.urls import path
from . import views
from .views import question

urlpatterns = [
    path('', views.question, name='home'),
]
