# Generated by Django 3.2.6 on 2021-09-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210904_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schema',
            name='name_schema',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
