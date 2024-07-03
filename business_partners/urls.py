from django.urls import path
from business_partners import views

urlpatterns =[
    path('', views.index, name='business_partners')
]