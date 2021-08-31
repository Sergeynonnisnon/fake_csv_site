from django import forms
from django.forms import ModelForm, modelform_factory
from django.http import HttpResponseRedirect

from .models import Schema,SchemaColumn,COLUMN_FIELD_CHOICES



class SchemaForm(forms.ModelForm):
    class Meta:
        model = Schema
        fields = '__all__'


class ColumnForm(forms.ModelForm):
    class Meta:
        model = SchemaColumn
        fields = '__all__'

