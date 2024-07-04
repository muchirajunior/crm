from django.shortcuts import render, redirect
from business_partners.models import BusinessPartner
from business_partners.forms import BusinessPartnerForm

def index(request):
    context ={
        'form': BusinessPartnerForm(),
        'partners': BusinessPartner.objects.all()
    }
    return render(request, 'business_partners.html', context=context)

def create_bp(request):
    if request.method == 'POST':
        form = BusinessPartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('business_partners')  # Redirect to a success page or wherever you want
    else:
        form = BusinessPartnerForm()

    return redirect('business_partners')