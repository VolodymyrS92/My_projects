from django.contrib import admin
from basic_app.models import NewSchema, SchemaColumns, DataSchemas
# Register your models here.
admin.site.register(NewSchema)
admin.site.register(SchemaColumns)
admin.site.register(DataSchemas)


