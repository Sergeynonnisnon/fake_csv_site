from django.db import models
from django.contrib.auth.models import User
# Create your models here.

COLUMN_FIELD_CHOICES = (
    ('Job', 'Job'),
    ('Email', 'Email'),
)
class Schema(models.Model):

    last_mod = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    column_cep = models.CharField(max_length=20, choices=(
        ('Comma(,)', ','),
        ('Semicolon(;)', ';')), default='Comma(,)')
    name_schema = models.CharField(max_length=200, unique=True)
    rows = models.IntegerField(default=1)
    column_field1 = models.CharField(max_length=20, choices=COLUMN_FIELD_CHOICES)


    def __str__(self):
        return self.name_schema

class Column(models.Model):
    name_schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    name_column = models.CharField(max_length=60)
    type_column = models.CharField(max_length=60, choices=COLUMN_FIELD_CHOICES)
    min_choise = models.IntegerField(blank=False, default=0)
    max_choise = models.IntegerField(blank=False, default=0)
    def __str__(self):
        return self.name_column