from django.contrib import admin
from .models import Schema,SchemaColumn
# Register your models here.

admin.site.register(Schema)

admin.site.register(SchemaColumn)