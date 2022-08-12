from django.contrib import admin

from .models import *

# Register your models here.


class EnquiryNoteAdmin(admin.ModelAdmin):
    list_display = ('added_time',)
    search_fields=('added_time',)
admin.site.register(EnquiryNote,EnquiryNoteAdmin)





class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('projectname','clientname','companyname')
    search_fields=('projectname',)
admin.site.register(Enquiry,EnquiryAdmin)

