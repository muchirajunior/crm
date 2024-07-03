from django.shortcuts import render

from business_partners.models import BusinessPartner

def index(request):
    
    return render(request, 'business_partners.html')