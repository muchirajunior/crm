from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from business_partners.models import BusinessPartner
from sales.models import SalesDocument, SalesDocumentItem
from salesreps.models import SalesEmployee
from stocks.models import Item

def sales_documents(request):
    documents = SalesDocument.objects.all()
    business_partners = BusinessPartner.objects.all()
    sales_employees = SalesEmployee.objects.all()
    return render(request, 'sales_documents.html', {'documents': documents, 'business_partners': business_partners, 'sales_employees': sales_employees})

def create_sales_document(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        object_code = request.POST.get('object_code')
        sales_employee = request.POST.get('sales_employee')

        try:
            selected_partner = BusinessPartner.objects.get(name=customer_name)
        except BusinessPartner.DoesNotExist:
            messages.error(request, "Selected partner does not exist.")
            return redirect('create_sales_document')

        # Use the code from the selected BusinessPartner
        customer_code = selected_partner.code

        try:
            document = SalesDocument.objects.create(customer_name=customer_name, customer_code=customer_code, object_code=object_code, sales_employee=sales_employee)
            messages.success(request, f"Sales Document '{document.number}' created successfully.")
            return redirect('sales_documents')
        except Exception as e:
            messages.error(request, f"Failed to create Sales Document: {e}")

 
    return redirect('sales_documents' )

def view_sales_document(request, document_id):
    document = get_object_or_404(SalesDocument, id=document_id)
    items = SalesDocumentItem.objects.filter(document=document)
    all_items = Item.objects.all()
    return render(request, 'view_sales_document.html', {'document': document, 'items': items, 'all_items': all_items})

def add_sales_document_item(request):
    if request.method == 'POST':
        document_id = request.POST.get('document_id')
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity'))

        try:
            document = SalesDocument.objects.get(id=document_id)
            item = Item.objects.get(id=item_id)
            SalesDocumentItem.objects.create(document=document, item_code=item.code, item_name=item.name, item_price=item.price, quantity=quantity)
            messages.success(request, "Item added successfully.")
        except Exception as e:
            messages.error(request, f"Failed to add item: {e}")

    return redirect('view_sales_document', document_id=document_id)

def remove_sales_document_item(request, item_id):
    item = get_object_or_404(SalesDocumentItem, id=item_id)
    document_id = item.document.id
    item.delete()
    messages.success(request, "Item removed successfully.")
    return redirect('view_sales_document', document_id=document_id)
