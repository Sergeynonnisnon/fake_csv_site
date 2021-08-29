from django.shortcuts import render
from django.http import HttpResponse


def login(response):
    return HttpResponse('login page be here')


def data_schemas(response):
    return HttpResponse('data schemas user be here')


def new_schema(response):
    return HttpResponse('new schema be here')


def data_sets(response):
    return HttpResponse('data sets be here')
