from django import forms
from django.forms import ModelForm, ValidationError
from django.utils import timezone
from .models import *

class ReceptForm(ModelForm):
    class Meta:
        model = Recept
        fields = '__all__'
        widgets = {
            'nev':forms.TextInput(attrs = {'class':'form-control'}),
            'kat_id':forms.Select(attrs = {'class':'form-control'}),
            'kep_eleresi_ut': forms.TextInput(attrs = {'class':'form-control'}),
            'leiras':forms.Textarea(attrs = {'class':'form-control'}),
            'hirdetes_datuma':forms.DateInput(format = '%Y-%m-%d', attrs={
                'type': 'date',
                'class':'form-control'
            })
        }

    def clean_hirdetes_datuma(self):
        hirdetes_datuma = self.cleaned_data.get('hirdetes_datuma', None)

        if(hirdetes_datuma is None):
            hirdetes_datuma = timezone.now().date()
        
        return hirdetes_datuma
        