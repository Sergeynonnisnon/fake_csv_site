from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Schema, Column
from .forms import LoginForm, NewShemaFormModel, ColumnForm, ColumnFormSet
import copy


# Create your views here.
def log_out(request):
    print('re')

    logout(request)
    return redirect('log_in')


def log_in(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            user = authenticate(username=cd['login'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)

                    return render(request, 'fake_csv_app/login.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'fake_csv_app/login.html', {'form': form, })


def data_schemas(request):
    if request.method == 'GET':
        sl = Schema.objects.filter(user=request.user)

        return render(request, 'fake_csv_app/data_schemas.html', {'sl': sl})
    else:
        if request.POST.get('new'):
            return redirect('new_schema')

        if request.POST.get('delete'):
            id = int(request.POST.get('delete').split('del-')[-1])

            col = Schema.objects.get(id=id).delete()

            sl = Schema.objects.filter(user=request.user)
            return render(request, 'fake_csv_app/data_schemas.html', {'sl': sl})


def new_schema(request):
    basicform = NewShemaFormModel()
    columnform = ColumnFormSet()
    if request.method == 'POST':
        basicform = NewShemaFormModel(request.POST)
        columnform = ColumnFormSet(request.POST)

        if columnform.is_valid() and basicform.is_valid():
            if request.POST.get('save'):
                # name_schema = basicform.cleaned_data['name_schema']
                instance = basicform.save(commit=False)
                instance.user = request.user

                instance.save()
                print(Schema.objects.get(name_schema=instance.name_schema))
                for form in columnform:
                    print(form.cleaned_data)
                    col = Column(
                        name_schema=Schema.objects.get(name_schema=instance.name_schema),
                        name_column=form.cleaned_data['name'],
                        type_column=form.cleaned_data['type_column'],
                        min_choise=form.cleaned_data['min_choise'],
                        max_choise=form.cleaned_data['max_choise'],
                    )
                    col.save()
            return redirect('data_schemas')

        return render(request, 'fake_csv_app/New_schema.html', {
            'basicform': basicform, 'columnform': columnform
        })
    else:
        return render(request, 'fake_csv_app/New_schema.html', {
            'basicform': basicform, 'columnform': columnform,

        })


def data_sets(request):
    return render(request, 'fake_csv_app/base.html', {})
