from django.urls import path
from sales import views

urlpatterns = [
    path('', views.sales_documents, name='sales_documents'),
    path('create_sales_document/', views.create_sales_document, name='create_sales_document'),
    path('view_sales_document/<int:document_id>/', views.view_sales_document, name='view_sales_document'),
    path('add_sales_document_item/', views.add_sales_document_item, name='add_sales_document_item'),
    path('remove_sales_document_item/<int:item_id>/', views.remove_sales_document_item, name='remove_sales_document_item'),
]
