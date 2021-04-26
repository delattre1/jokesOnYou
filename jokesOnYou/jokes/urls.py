from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/joke/', views.api_joke),
]
