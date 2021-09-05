# Generated by Django 3.2.6 on 2021-08-31 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_mod', models.DateTimeField(auto_now=True)),
                ('column_cep', models.CharField(choices=[('Comma(,)', ','), ('Semicolon(;)', ';')], default='Comma(,)', max_length=20)),
                ('name_schema', models.CharField(max_length=200)),
                ('rows', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='SchemaColumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_field', models.CharField(choices=[('Job', 'Job'), ('Email', 'Email')], max_length=20)),
                ('Schema', models.ManyToManyField(to='main.Schema')),
            ],
        ),
    ]
