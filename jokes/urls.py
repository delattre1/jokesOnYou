from django.urls import path

from . import views

urlpatterns = [
    path('joke/', views.api_joke),
    path('favorites/', views.api_favorites),
]
