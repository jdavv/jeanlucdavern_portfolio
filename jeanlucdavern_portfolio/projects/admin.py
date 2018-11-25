from django.contrib import admin
from .models import Project, Keywords


class KeywordsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name', ),
    }


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title', ),
    }


admin.site.register(Project, ProjectAdmin)
admin.site.register(Keywords, KeywordsAdmin)
