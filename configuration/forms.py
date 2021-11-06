from django import forms
from django.forms import ModelForm
from. models import CompanyInfo


class CompanyInfoForm(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields = '__all__'








