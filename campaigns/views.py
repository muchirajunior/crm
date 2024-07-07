from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from campaigns.models import Campaign

def create_campaign(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        budget = request.POST.get('budget')
        description = request.POST.get('description')

        try:
            Campaign.objects.create(
                name=name,
                start_date=start_date,
                end_date=end_date,
                budget=budget,
                description=description
            )

            messages.success(request, "Campaign created successfully.")
            return redirect('list_campaigns')
        
        except Exception as e:
            messages.error(request, f"Error creating campaign: {e}")
            return redirect('create_campaign')

    return redirect('list_campaigns')

def list_campaigns(request):
    campaigns = Campaign.objects.all()
    return render(request, 'list_campaigns.html', {'campaigns': campaigns})
  

def update_campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    if request.method == 'POST':
        try:
            campaign.name = request.POST.get('name')
            campaign.start_date = request.POST.get('start_date')
            campaign.end_date = request.POST.get('end_date')
            campaign.budget = request.POST.get('budget')
            campaign.description = request.POST.get('description')

            campaign.save()
            messages.success(request, "Campaign updated successfully.")
            return redirect('list_campaigns')
        
        except Exception as e:
            messages.error(request, f"Error updating campaign: {e}")
            return redirect('update_campaign', campaign_id=campaign_id)

    return redirect('list_campaigns')
