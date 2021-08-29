from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name='login'),
    path("new_schema/", views.new_schema, name="new_schema"),
    path("data_schemas/", views.data_schemas, name="data_schemas"),
    path("data_sets/", views.data_sets, name="data_sets"),
]
