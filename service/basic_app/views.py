from django.shortcuts import render
from .forms import NewSchemaForm, SecondSchema, DataSchemasForm


def data_schema(request):
    first_schema = DataSchemasForm
    return render(request,'basic_app/schema_form.html', {'first_schema': first_schema})



def form_name_view(request):
    schema = NewSchemaForm()
    new_schema = SecondSchema()
    return render(request,'basic_app/index.html', {'new_schema': new_schema, 'schema': schema})


# def new_form(request):
#     new_schema = SecondSchema()
#     return render(request, 'basic_app/index.html', {'new_schema': new_schema})