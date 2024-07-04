from django import forms
from business_partners.models import BusinessPartner

class BusinessPartnerForm(forms.ModelForm):
    class Meta:
        model = BusinessPartner
        fields = [ 'code', 'name', 'contact_person', 'email', 'phone', 'address', 'type']
