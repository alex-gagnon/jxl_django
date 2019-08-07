from django.contrib import admin

# Register your models here.
from .models import Project, Filter


class FilterInLine(admin.TabularInline):
    model = Filter
    extra = 1


class JXLAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields': ['pub_date']}),
        ('Projects', {'fields': ['project_text', 'project_code']}),
    ]
    list_display = ('project_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['project_text']
    inlines = [FilterInLine]


admin.site.register(Project, JXLAdmin)
