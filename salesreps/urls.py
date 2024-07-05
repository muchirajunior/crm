from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales_employees, name='sales_employees'),
    path('create_sales_employee/', views.create_sales_employee, name='create_sales_employee'),
    path('update_sales_employee/', views.update_sales_employee, name='update_sales_employee'),
]
