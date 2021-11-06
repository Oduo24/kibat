from django import forms
from django.forms import ModelForm
from. models import InventoryItem


class AddItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = '__all__'








