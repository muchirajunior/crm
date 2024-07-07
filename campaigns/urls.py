from django.urls import path
from .views import create_campaign, list_campaigns, update_campaign

urlpatterns = [
    path('', list_campaigns, name='list_campaigns'),
    path('create/', create_campaign, name='create_campaign'),
    path('update/<int:campaign_id>/', update_campaign, name='update_campaign'),
]
