from django.db import models
from django.forms import ModelForm

# Create your models here.
COLUMN_CHOICES = (
    ('Job', 'Job'),
    ('Email', 'Email'),
)


class SchemaList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Schema(models.Model):
    SchemaList = models.ForeignKey(SchemaList, on_delete=models.CASCADE)
    last_mod = models.DateTimeField(auto_now=True)
    column_cep = models.CharField(max_length=20, choices=(
        ('Comma(,)', ','),
        ('Semicolon(;)', ';')), default='Comma(,)')
    name_schema = models.CharField(max_length=200)
    rows = models.IntegerField(default=1)

    def __str__(self):
        return self.name_schema


class SchemaColumn(models.Model):
    name_schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    column_field = models.CharField(max_length=20, choices=COLUMN_CHOICES)

    def __str__(self):
        return self.column_field


class SchemaForm(ModelForm):
    class Meta:
        model = Schema
        fields = ['column_cep', 'name_schema', 'rows']


class ColumnForm(ModelForm):
    class Meta:
        model = SchemaColumn
        fields = ['column_field', ]
