from django.db import models


# Create your models here.

class NewSchema(models.Model):
    name = models.CharField(max_length=264, blank=True)
    column_separator = models.CharField(max_length=264, blank=True)
    string_character = models.CharField(max_length=264, blank=True)

    def __str__(self):
        return self.name


class SchemaColumns(models.Model):
    schemacolumn = models.ForeignKey(NewSchema, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, unique=True, blank=True)
    job = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    domain_name = models.CharField(max_length=254, unique=True)
    phone_number = models.IntegerField(unique=True)
    company_name = models.CharField(max_length=254, unique=True)
    text = models.CharField(max_length=254, unique=True)
    specific_integer = models.IntegerField(unique=True)
    address = models.CharField(max_length=264, unique=True)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.schemacolumn)


class DataSchemas(models.Model):
    data_schemas = models.ForeignKey(NewSchema, on_delete=models.CASCADE, default='x')
    title = models.CharField(max_length=100)
    modified = models.CharField(max_length=100, unique=True)
    actions = models.CharField(max_length=100)

    def __str__(self):
        return str(self.data_schemas)
