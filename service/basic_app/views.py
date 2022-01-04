from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'basic_app/index.html')


def form_nane_view(request):
    schema = forms.SchemaColumns()
    return render(request, 'basic_app/form_page.html', {"schema": schema})
