from django.contrib import admin
from .models import SchemaList, Schema,SchemaColumn
# Register your models here.
admin.site.register(SchemaList)
admin.site.register(Schema)

admin.site.register(SchemaColumn)