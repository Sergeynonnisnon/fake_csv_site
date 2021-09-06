from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect
from django.http import FileResponse
from .models import Schema, Column, Sets
from .forms import LoginForm, NewShemaFormModel, ColumnFormSet, SetForm
from .tasks import create_csv

import os
from django.conf import settings
from django.http import HttpResponse


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
    setform = SetForm()
    setform.fields['name_schema'].queryset = Schema.objects.filter(user=request.user)
    sl = Sets.objects.filter(user=request.user)

    if request.method == 'GET':
        return render(request, 'fake_csv_app/data_sets.html', {'sl': sl, 'setform': setform})

    else:

        if request.POST.get('download'):
            path = request.POST.get('download').split('-')[-1]

            file_path = os.path.join(settings.MEDIA_ROOT, f'{path}.csv')
            print(file_path)

            if os.path.exists(file_path):

                with open(file_path, 'rb'):
                    response = FileResponse(open(file_path, 'rb'))
                    return response
            else:
                return render(request, 'fake_csv_app/data_sets.html', {'sl': sl, 'setform': setform})


        if request.POST.get('save'):

            # request.post.name_schema return id schema in db
            setform = SetForm(request.POST)
            if setform.is_valid():
                instanse = Sets(
                    user=request.user,
                    name_schema=setform.cleaned_data.get('name_schema'),
                    rows=request.POST.get('row'),
                    status='Processed')
                instanse.save()
                print(instanse.id)

                create_csv.delay(instanse.id)

            return redirect('data_sets')
