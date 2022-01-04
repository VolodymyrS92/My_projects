# Generated by Django 3.2.7 on 2022-01-03 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewSchema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='number', max_length=264)),
                ('column_separator', models.CharField(default='number', max_length=264)),
                ('string_character', models.CharField(default='number', max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='SchemaColumns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=200, unique=True)),
                ('job', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('domain_name', models.CharField(max_length=254, unique=True)),
                ('phone_number', models.IntegerField(unique=True)),
                ('company_name', models.CharField(max_length=254, unique=True)),
                ('text', models.CharField(max_length=254, unique=True)),
                ('specific_integer', models.IntegerField(unique=True)),
                ('address', models.CharField(max_length=264, unique=True)),
                ('date', models.DateField()),
                ('schemacolumn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.newschema')),
            ],
        ),
    ]