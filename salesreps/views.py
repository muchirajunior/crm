from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SalesEmployee

def sales_employees(request):
    employees = SalesEmployee.objects.all()
    return render(request, 'sales_employees.html', {'employees': employees})

def create_sales_employee(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        try:
            employee = SalesEmployee.objects.create(code=code, name=name, email=email, phone=phone)
            messages.success(request, f"Sales Employee '{employee.name}' created successfully.")
            return redirect('sales_employees')
        except Exception as e:
            messages.error(request, f"Failed to create Sales Employee: {e}")

    return redirect('sales_employees')

def update_sales_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('id')
        code = request.POST.get('code')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        try:
            employee = SalesEmployee.objects.get(id=employee_id)
            employee.code = code
            employee.name = name
            employee.email = email
            employee.phone = phone
            employee.save()
            messages.success(request, f"Sales Employee '{employee.name}' updated successfully.")
            return redirect('sales_employees')
        except SalesEmployee.DoesNotExist:
            messages.error(request, "Sales Employee not found.")
        except Exception as e:
            messages.error(request, f"Failed to update Sales Employee: {e}")

    return redirect('sales_employees')
