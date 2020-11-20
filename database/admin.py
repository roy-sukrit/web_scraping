from django.contrib import admin
from database.models import myData
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(myData)
class imagedb(ImportExportModelAdmin):
    pass
