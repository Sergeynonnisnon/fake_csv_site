from django.db import models
from django.forms import ModelForm

# Create your models here.
COLUMN_FIELD_CHOICES = (
    ('Job', 'Job'),
    ('Email', 'Email'),
)
ORDER_CHOISES=(
    (1, 1),
    (2, 2),
)

class Schema(models.Model):

    last_mod = models.DateTimeField(auto_now=True)
    column_cep = models.CharField(max_length=20, choices=(
        ('Comma(,)', ','),
        ('Semicolon(;)', ';')), default='Comma(,)')
    name_schema = models.CharField(max_length=200)
    rows = models.IntegerField(default=1)

    def __str__(self):
        return self.name_schema


class SchemaColumn(models.Model):
    Schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    order_by = models.IntegerField (choices=ORDER_CHOISES)
    column_field = models.CharField(max_length=20, choices=COLUMN_FIELD_CHOICES)

    def __str__(self):
        return self.column_field


