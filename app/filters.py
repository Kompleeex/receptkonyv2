import django_filters as filters
from django import forms

from .models import *

class ReceptFilter(filters.FilterSet):
    kat_id = filters.ModelChoiceFilter(
        label = 'Kategoria',
        field_name = 'kat_id',
        to_field_name = 'id',
        queryset = Kategoriak.objects.all(),
        widget = forms.Select(attrs = {
            'class': 'form-control'}
        )
    )
    
    class Meta:
        model = Recept
        fields = ['kat_id']