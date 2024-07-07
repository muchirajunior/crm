from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from business_partners.models import BusinessPartner
from opportunities.models import Opportunity
from salesreps.models import SalesEmployee

def create_opportunity(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        stage = request.POST.get('stage')
        amount = request.POST.get('amount')
        close_date = request.POST.get('close_date')
        description = request.POST.get('description')
        business_partner_id = request.POST.get('business_partner')
        sales_person = request.POST.get('sales_person')

        try:
            business_partner = BusinessPartner.objects.get(id=business_partner_id)
            Opportunity.objects.create(
                name=name,
                stage=stage,
                amount=amount,
                close_date=close_date,
                description=description,
                business_partner=business_partner,
                sales_person=sales_person
            )

            messages.success(request, "Opportunity created successfully.")
            return redirect('list_opportunities')
        
        except Exception as e:
            messages.error(request, f"Error creating opportunity: {e}")
            return redirect('list_opportunities')

   
    return redirect('list_opportunities')

def list_opportunities(request):

    opportunities = Opportunity.objects.all()
    business_partners = BusinessPartner.objects.all()
    sales_employees = SalesEmployee.objects.all()
    return render(request, 'list_opportunities.html', {'opportunities': opportunities, 'business_partners': business_partners, 'sales_employees': sales_employees})
   

def update_opportunity(request, opportunity_id):
    opportunity = get_object_or_404(Opportunity, id=opportunity_id)

    if request.method == 'POST':
        try:
            opportunity.name = request.POST.get('name')
            opportunity.stage = request.POST.get('stage')
            opportunity.amount = request.POST.get('amount')
            opportunity.close_date = request.POST.get('close_date')
            opportunity.description = request.POST.get('description')
            opportunity.business_partner = BusinessPartner.objects.get(id=request.POST.get('business_partner'))
            opportunity.sales_person = request.POST.get('sales_person')

            opportunity.save()
            messages.success(request, "Opportunity updated successfully.")
            return redirect('list_opportunities')
        
        except Exception as e:
            messages.error(request, f"Error updating opportunity: {e}")
            return redirect('update_opportunity', opportunity_id=opportunity_id)

    return redirect('list_opportunities')