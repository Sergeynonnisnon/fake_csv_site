from django import forms
from .models import Schema, COLUMN_FIELD_CHOICES , Column
from django.forms import formset_factory, modelformset_factory
class LoginForm(forms.Form):
    login = forms.CharField(max_length=20, required=True)
    password = forms.CharField(max_length=20, required=True)

class NewShemaFormModel(forms.ModelForm):
    class Meta:
        model = Schema
        fields = ('name_schema',

                  'column_cep',
                  'string_character',

                  )


class ColumnForm(forms.Form):

    name = forms.CharField(
                                  label='Column',
                                  widget=forms.TextInput(attrs={
                                      'class': 'form-control',
                                      'placeholder': 'Enter name column here'
                                  }))

    type_column = forms.ChoiceField(choices=COLUMN_FIELD_CHOICES,
                                    widget=forms.Select)

    min_choise = forms.IntegerField()
    max_choise = forms.IntegerField()

class SetForm(forms.Form):

    name_schema = forms.ModelChoiceField(queryset=Schema.objects.all(),
                                    widget=forms.Select)

ColumnFormSet = formset_factory(ColumnForm, extra=1)
