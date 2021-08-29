from django.contrib import admin
from .models import schema_list, schema
# Register your models here.
admin.site.register(schema_list)
admin.site.register(schema)

