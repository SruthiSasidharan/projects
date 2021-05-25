from .models import Brand,Mobiles
from django import forms
from django.forms import ModelForm

class BrandCreateForm(forms.ModelForm):
    class Meta:
        model=Brand
        fields='__all__'


class MobileCreateForm(forms.ModelForm):
    class Meta:
        model=Mobiles
        fields='__all__'

class MobileUpdateForm(forms.ModelForm):
    class Meta:
        model=Mobiles
        fields='__all__'