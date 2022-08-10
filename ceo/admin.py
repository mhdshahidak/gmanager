from django.contrib import admin

from .models import *

# Register your models here.


class CatagotyAdmin(admin.ModelAdmin):
    list_display = ('catagoty_title',)
    search_fields=('catagoty_title',)
admin.site.register(Catagoty,CatagotyAdmin)


class SubCatagoryAdmin(admin.ModelAdmin):
    list_display = ('catagoty','title')
    search_fields=('title',)
admin.site.register(SubCatagory,SubCatagoryAdmin)


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'catagoty' )
    search_fields=('title',)
admin.site.register(Employees,EmployeesAdmin)


class EmergenctContactAdmin(admin.ModelAdmin):
    list_display = ('primarycontact_name','relation', 'employee')
    search_fields=('title',)
admin.site.register(EmergenctContact,EmergenctContactAdmin)


