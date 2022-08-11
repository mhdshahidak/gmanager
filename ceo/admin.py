from django.contrib import admin

from .models import *

# Register your models here.


class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('catagory_title',)
    search_fields=('catagory_title',)
admin.site.register(Catagory,CatagoryAdmin)


class SubCatagoryAdmin(admin.ModelAdmin):
    list_display = ('catagory','title')
    search_fields=('title',)
admin.site.register(SubCatagory,SubCatagoryAdmin)


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'catagory' )
    search_fields=('title',)
admin.site.register(Employees,EmployeesAdmin)


class EmergenctContactAdmin(admin.ModelAdmin):
    list_display = ('primarycontact_name','relation', 'employee')
    search_fields=('title',)
admin.site.register(EmergenctContact,EmergenctContactAdmin)


admin.site.register(User)


