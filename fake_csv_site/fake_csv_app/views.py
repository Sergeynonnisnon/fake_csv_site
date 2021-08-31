from django.forms import formset_factory
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import UpdateView

from .models import Schema, SchemaColumn
from .forms import SchemaForm, ColumnForm
from django.forms import modelformset_factory, inlineformset_factory


def login(response):
    return HttpResponse('login page be here')


def data_schemas(response):
    #sl = SchemaList.objects.get(name='testlist')
    sl=9
    return render(response, 'fake_csv_app/data_schemas.html', {'sl': sl})


def new_schema(response):
    schema_form = ColumnForm()
    if response.method == "POST":
        schema_form = ColumnForm(response.POST)
        if schema_form.is_valid():
            schema_form.save()
    return render(response, 'fake_csv_app/New_schema.html',
                  {'basicform': schema_form})


def data_sets(response):
    return render(response, 'fake_csv_app/base.html', {})



