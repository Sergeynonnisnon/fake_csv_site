import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

COLUMN_FIELD_CHOICES = (

    ('Full name', 'Full name'),
    ('Job', 'Job'),
    ('Email', 'Email'),
    ('Domain name', 'Domain name'),
    ('Phone number', 'Phone number'),
    ('Company name', 'Company name'),
    ('Text', 'Text'),
    ('Integer', 'Integer'),
    ('Address', 'Address'),
    ('Date', 'Date'),

)


class Schema(models.Model):
    last_mod = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    column_cep = models.CharField(max_length=20, choices=(
        ('Comma(,)', ','),
        ('Semicolon(;)', ';')), default='Comma(,)')
    string_character = models.CharField(max_length=20, choices=(
        (r'"', r'"'),
        (r"'", r"'")), default=r'"')
    name_schema = models.CharField(max_length=200, unique=True, default=uuid.uuid1)

    column_field1 = models.CharField(max_length=20, choices=COLUMN_FIELD_CHOICES)

    def __str__(self):
        return self.name_schema


class Column(models.Model):
    name_schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    name_column = models.CharField(max_length=60)
    type_column = models.CharField(max_length=60, choices=COLUMN_FIELD_CHOICES)
    min_choise = models.IntegerField( default=0, blank=True)
    max_choise = models.IntegerField( default=0, blank=True)

    def __str__(self):
        return self.name_column

SET_STATUSE_CHOISES=(

    ('Not send', 'Not send'),
    ('Processed', 'Processed'),
    ('Ready', 'Ready'),
)

class Sets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=SET_STATUSE_CHOISES)
    id_schema = models.ForeignKey(Schema, to_field='id', on_delete=models.CASCADE)
    download_link = models.CharField(max_length=200, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_schema