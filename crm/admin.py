from django.contrib import admin

from .models import *
from ceo.models import *

# Register your models here.


class EnquiryNoteAdmin(admin.ModelAdmin):
    list_display = ('added_time',)
    search_fields=('added_time',)
admin.site.register(EnquiryNote,EnquiryNoteAdmin)





class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('projectname','clientname','companyname')
    search_fields=('projectname',)
admin.site.register(Enquiry,EnquiryAdmin)



class ClientAdmin(admin.ModelAdmin):
    list_display = ('name','companyname','phone')
    search_fields=('name',)
admin.site.register(Client,ClientAdmin)