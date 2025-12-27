from django.urls import path
from . import views

urlpatterns = [
    path("can-i-flex/", views.calculate_budget),
]
