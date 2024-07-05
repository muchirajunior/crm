from django.urls import path

from stocks import views


urlpatterns = [
    path('',views.index,name='stocks'),
    path('create', views.create_item,name='create_item'),
    path('update_item', views.update_item, name='update_item'),
]