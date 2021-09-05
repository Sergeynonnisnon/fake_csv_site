from django.urls import path
from . import views

urlpatterns = [
    path("", views.log_in, name='log_in'),
    path("new_schema/", views.new_schema, name="new_schema"),
    path("data_schemas/", views.data_schemas, name="data_schemas"),
    path("data_sets/", views.data_sets, name="data_sets"),
    path("log_out/", views.log_out, name="log_out"),
]
