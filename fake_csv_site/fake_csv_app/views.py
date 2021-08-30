from django.shortcuts import render
from django.http import HttpResponse
from .models import SchemaList,Schema,SchemaForm , ColumnForm
from .forms import New_Schema
def login(response):
    return HttpResponse('login page be here')


def data_schemas(response):
    sl = SchemaList.objects.get(name='testlist')

    return render(response, 'fake_csv_app/data_schemas.html', {'sl': sl})


def new_schema(response):
    if response.method == 'POST':
        column_form = SchemaForm(response.POST)
        if column_form .is_valid():
            n = column_form.cleaned_data['name_schema']
            print(n)
            return render(response, 'fake_csv_app/New_schema.html', {'column_form': column_form})

    else:
        basic_form = SchemaForm
        column_form = ColumnForm
        forms = {'basic_form': basic_form ,'column_form':column_form}
        return render(response, 'fake_csv_app/New_schema.html',forms)


def data_sets(response):
    return render(response, 'fake_csv_app/base.html', {})
