from django.urls import path
from activities.views import create_activity, list_activities, update_activity

urlpatterns = [
    path('', list_activities, name='list_activities'),
    path('activities/create/', create_activity, name='create_activity'),
    path('activities/update/<int:activity_id>/', update_activity, name='update_activity'),
]
