from django.shortcuts import get_object_or_404, render, redirect
from business_partners.models import BusinessPartner
from business_partners.forms import BusinessPartnerForm
from django.contrib import messages

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

def update_business_partner(request, partner_id):
    business_partner = get_object_or_404(BusinessPartner, id=partner_id)

    if request.method == 'POST':
        business_partner.code = request.POST.get('code')
        business_partner.name = request.POST.get('name')
        business_partner.contact_person = request.POST.get('contact_person')
        business_partner.email = request.POST.get('email')
        business_partner.phone = request.POST.get('phone')
        business_partner.address = request.POST.get('address')
        business_partner.type = request.POST.get('type')

        try:
            business_partner.save()
            messages.success(request, "Business Partner updated successfully.")
        except Exception as e:
            messages.error(request, f"Error updating Business Partner: {e}")

        return redirect('business_partners')
    
    return redirect('business_partners')
