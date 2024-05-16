from django import forms
from .models import company_master


class company_master_form(forms.ModelForm):
    class Meta:
        model=company_master
        fields=['companyname','address','mailid','phone','state','district','gst']
