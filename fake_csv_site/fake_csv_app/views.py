from django.shortcuts import render
from django.http import HttpResponse
from .models import schema_list,schema

def login(response):
    return HttpResponse('login page be here')


def data_schemas(response):
    sl = schema_list.objects.get(name='testlist')

    return render(response, 'fake_csv_app/data_schemas.html', {'sl': sl})


def new_schema(response):
    return render(response, 'fake_csv_app/base.html', {})


def data_sets(response):
    return render(response, 'fake_csv_app/base.html', {})
