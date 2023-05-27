from datetime import date

from django_filters import FilterSet, DateFilter, CharFilter
from django import forms

from .models import *


class OrderFilter(FilterSet):
    personal_index = CharFilter(
        field_name='workers__personal_index',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    creation_date = DateFilter(
        field_name='creation_date',
        widget=forms.DateInput(attrs={'class': 'form-control',
                                      'type': 'date',
                                      'value': date.today().strftime('%Y-%m-%d')}),
        lookup_expr='startswith'
    )

    class Meta:
        model = WorkingOrder
        fields = ['personal_index', 'creation_date']