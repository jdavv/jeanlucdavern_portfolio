from django.contrib import admin
from .models import About, SharingMeta, Project, Keywords, Social


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


class SharingMetaAdmin(admin.ModelAdmin):
    pass


class SocialAdmin(admin.ModelAdmin):
    pass


admin.site.register(Social, SocialAdmin)
admin.site.register(SharingMeta, SharingMetaAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Keywords, KeywordsAdmin)
