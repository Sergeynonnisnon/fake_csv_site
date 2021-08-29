from django.db import models

# Create your models here.



class schema_list(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class schema(models.Model):
    schema_list = models.ForeignKey(schema_list, on_delete=models.CASCADE)
    name_schema = models.CharField(max_length=200)
    rows = models.IntegerField(default=1)
    Job = models.BooleanField(default=False)
    Email = models.BooleanField(default=False)
    Domain = models.BooleanField(default=False)
    Company = models.BooleanField(default=False)
    Text = models.BooleanField(default=False)  # TODO range
    Integer = models.BooleanField(default=False)  # TODO range
    Address = models.BooleanField(default=False)
    Date = models.BooleanField(default=False)
    def __str__(self):
        return self.name_schema
