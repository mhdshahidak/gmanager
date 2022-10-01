from django.contrib import admin

from .models import (
    SRS,
    DailyProgress,
    Meeting,
    Praposalpdf,
    Project,
    ProjectMembers,
    ProjectProgressFiles,
    ProjectStatus,
    Reworks,
    Task,
    Updation,
)

# Register your models here.


class PraposalpdfAdmin(admin.ModelAdmin):
    list_display = ("enquiry",)
    search_fields = ("enquiry",)


admin.site.register(Praposalpdf, PraposalpdfAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("projectname",)
    search_fields = ("projectname",)


admin.site.register(Project, ProjectAdmin)


class ProjectMembersAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "lead",
    )
    search_fields = ("project",)


admin.site.register(ProjectMembers, ProjectMembersAdmin)


admin.site.register(Meeting)

admin.site.register(SRS)

admin.site.register(ProjectStatus)

admin.site.register(ProjectProgressFiles)

admin.site.register(DailyProgress)


admin.site.register(Updation)


admin.site.register(Reworks)

admin.site.register(Task)
