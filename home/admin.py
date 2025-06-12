from django.contrib import admin
from .models import ContentBlock
from django_summernote.admin import SummernoteModelAdmin

@admin.register(ContentBlock)
class ContentBlockAdmin(SummernoteModelAdmin):

    list_display = ('title', 'content', 'section', 'order', 'publish')
    list_editable = ('section', 'order', 'publish')
    search_fields = ['title','section','publish']
    list_filter = ('section','publish')
    summernote_fields = ('content',)
    ordering = ('order',)