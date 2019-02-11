from django.urls import path

from . import views

urlpatterns = [
        path('input', views.input),
]

