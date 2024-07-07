from django.urls import path
from .views import create_opportunity, list_opportunities, update_opportunity

urlpatterns = [
    path('create/', create_opportunity, name='create_opportunity'),
    path('', list_opportunities, name='list_opportunities'),
    path('update/<int:opportunity_id>/', update_opportunity, name='update_opportunity'),
]
