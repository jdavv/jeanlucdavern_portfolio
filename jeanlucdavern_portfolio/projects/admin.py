from django.contrib import admin
from .models import About, Project, Keywords


class KeywordsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name', ),
    }


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title', ),
    }


class AboutAdmin(admin.ModelAdmin):
    pass


admin.site.register(About, AboutAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Keywords, KeywordsAdmin)
