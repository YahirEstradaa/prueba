from django.urls import path
from . import views

urlpatterns = [
    path('mostrar-customers/', views.mostrar_customers, name='mostrar_customers'),
]
