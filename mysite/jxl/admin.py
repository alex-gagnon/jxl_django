from django.contrib import admin

# Register your models here.
from .models import JXLModel


class JXLAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Projects', {'fields': ['project_text', 'project_code']}),
        ('Filter by', {'fields': ['filter_by_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('project_text', 'pub_date', 'was_published_recently')


admin.site.register(JXLModel, JXLAdmin)
