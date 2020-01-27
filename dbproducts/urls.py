from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("research_substitute/", views.research_substitute, name="research_substitute"),
    path("details/<int:product_id>/", views.detail, name="detail"),
]
