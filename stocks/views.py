from django.contrib import messages
from django.shortcuts import redirect, render

from stocks.models import Item

def index(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'items.html', context=context)

def create_item(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        try:
            # Create the item
            item = Item.objects.create(name=name, code=code, quantity=quantity, price=price)
            messages.success(request, f"Item '{item.name}' created successfully.")
            return redirect('stocks')  # Redirect to your stocks route
        except Exception as e:
            messages.error(request, f"Failed to create item: {e}")

            return redirect('stocks')
        
def update_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('id')
        name = request.POST.get('name')
        code = request.POST.get('code')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        try:
            item = Item.objects.get(id=item_id)
            item.name = name
            item.code = code
            item.quantity = quantity
            item.price = price
            item.save()
            messages.success(request, f"Item '{item.name}' updated successfully.")
            return redirect('stocks')
        except Item.DoesNotExist:
            messages.error(request, "Item not found.")
        except Exception as e:
            messages.error(request, f"Failed to update item: {e}")

    return redirect('stocks')
