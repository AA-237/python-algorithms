from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("objective/<int:id>", views.objective_details, name="objective_details")
]
