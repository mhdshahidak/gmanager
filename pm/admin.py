from django.contrib import admin

from .models import *

# Register your models here.


class PraposalpdfAdmin(admin.ModelAdmin):
    list_display = ('enquiry',)
    search_fields=('enquiry',)
admin.site.register(Praposalpdf,PraposalpdfAdmin)
