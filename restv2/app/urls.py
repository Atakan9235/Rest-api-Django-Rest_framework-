from django.urls import path
from . import views

urlpatterns = [
    path('', views.veriler),
    path('add', views.gonder),
    path('<int:pk>/', views.detay),
    
]
