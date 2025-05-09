from django.shortcuts import render

from .models import Customer  # Importa el modelo Customer

def mostrar_customers(request):
    # Obtener todos los registros de la tabla Customers
    customers = Customer.objects.all()
    return render(request, 'mostrar_customers.html', {'customers': customers})
