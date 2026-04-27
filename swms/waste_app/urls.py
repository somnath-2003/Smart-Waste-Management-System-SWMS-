from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('route/', views.route_view),
]
