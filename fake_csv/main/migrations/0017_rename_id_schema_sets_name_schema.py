# Generated by Django 3.2.6 on 2021-09-05 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_sets_create_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sets',
            old_name='id_schema',
            new_name='name_schema',
        ),
    ]