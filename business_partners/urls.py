from django.urls import path
from business_partners import views

urlpatterns =[
    path('', views.index, name='business_partners'),
    path('create', views.create_bp, name='create_bp'),
    path('update/<int:partner_id>/', views.update_business_partner, name='update_business_partner'),
]