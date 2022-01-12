from django import forms
from .models import NewSchema, SchemaColumns


class NewSchemaForm(forms.ModelForm):
    class Meta:
        model = NewSchema
        fields = ('name', 'column_separator', 'string_character')


class SecondSchema(forms.ModelForm):
    class Meta:
        model = SchemaColumns
        fields = ('full_name', 'job', 'email', 'domain_name', 'phone_number', 'company_name',
                  'text', 'specific_integer', 'address', 'date')


