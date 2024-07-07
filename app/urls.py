from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('business-partners/', include('business_partners.urls')),
    path('stocks-management/', include('stocks.urls')),
    path('sales-employees/', include('salesreps.urls')),
    path('sales-documents/',include('sales.urls')),
    path('activities/',include('activities.urls'))
]
