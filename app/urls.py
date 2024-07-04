from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('business-partners/', include('business_partners.urls')),
    path('stocks-management/', include('stocks.urls'))
]
