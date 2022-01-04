from django.shortcuts import render
from .forms import NewSchemaForm, SecondSchema


def form_name_view(request):
    schema = NewSchemaForm()
    return render(request, 'basic_app/index.html', {"schema": schema})


def new_form(request):
    new_schema = SecondSchema()
    return render(request, 'basic_app/index.html', {'new_schema': new_schema})
