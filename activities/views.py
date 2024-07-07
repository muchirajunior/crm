from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from activities.models import Activity
from business_partners.models import BusinessPartner
from sales.models import SalesDocument
from salesreps.models import SalesEmployee

def create_activity(request):
    if request.method == 'POST':
        sales_person_name = request.POST.get('sales_person_name')
        business_partner_id = request.POST.get('business_partner')
        sales_document_id = request.POST.get('sales_document')
        activity_type = request.POST.get('activity_type')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        date = request.POST.get('date')
        description = request.POST.get('description')

        try:
            business_partner = get_object_or_404(BusinessPartner, id=business_partner_id)
            sales_document = get_object_or_404(SalesDocument, id=sales_document_id)

            Activity.objects.create(
                sales_person_name=sales_person_name,
                business_partner=business_partner,
                sales_document=sales_document,
                activity_type=activity_type,
                start_time=start_time,
                end_time=end_time,
                date=date,
                description=description
            )

            messages.success(request, "Activity created successfully.")
            return redirect('list_activities')
        
        except Exception as e:
            messages.error(request, f"Error creating activity: {e}")
            return redirect('list_activities')
    
    return redirect('list_activities')

def list_activities(request):
    activities = Activity.objects.all()

    business_partners = BusinessPartner.objects.all()
    sales_documents = SalesDocument.objects.all()
    sales_employees = SalesEmployee.objects.all()

    return render(request, 'list_activities.html', {
        'activities': activities,
        'business_partners': business_partners,
        'sales_documents': sales_documents,
        'sales_employees': sales_employees
    })
    

def update_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    print(f'Updating activity ${activity_id}')

    if request.method == 'POST':
        try:
            activity.sales_person_name = request.POST.get('sales_person_name')
            business_partner_id = request.POST.get('business_partner')
            sales_document_id = request.POST.get('sales_document')
            activity.activity_type = request.POST.get('activity_type')
            activity.start_time = request.POST.get('start_time')
            activity.end_time = request.POST.get('end_time')
            activity.date = request.POST.get('date')
            activity.description = request.POST.get('description')

            activity.business_partner = get_object_or_404(BusinessPartner, id=business_partner_id)
            activity.sales_document = get_object_or_404(SalesDocument, id=sales_document_id)

            activity.save()
            messages.success(request, "Activity updated successfully.")
            return redirect('list_activities')
        
        except Exception as e:
            messages.error(request, f"Error updating activity: {e}")
            return redirect('list_activities')

   

    return  redirect('list_activities')
