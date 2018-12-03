from django import forms
from testadmin.models import movie,customer

class myform(forms.ModelForm):
    class Meta:
        model=movie
        fields="__all__"

class model_form(forms.ModelForm):
    class Meta:
        model=customer
        fields="__all__"
