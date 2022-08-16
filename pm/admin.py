from django.contrib import admin

from .models import *

# Register your models here.


class PraposalpdfAdmin(admin.ModelAdmin):
    list_display = ('enquiry',)
    search_fields=('enquiry',)
admin.site.register(Praposalpdf,PraposalpdfAdmin)





class ProjectAdmin(admin.ModelAdmin):
    list_display = ('projectname',)
    search_fields=('projectname',)
admin.site.register(Project,ProjectAdmin)




class ProjectMembersAdmin(admin.ModelAdmin):
    list_display = ('project','lead',)
    search_fields=('project',)
admin.site.register(ProjectMembers,ProjectMembersAdmin)
