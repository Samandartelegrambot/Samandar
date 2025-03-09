from django.contrib import admin
from django.utils.html import format_html
from .models import TranslationHistory, Advertisement, ContactSubmission


class TranslationHistoryAdmin(admin.ModelAdmin):
    list_display = ('direction', 'original_text_short', 'translated_text_short', 'file_name', 'file_extension', 'created_at')
    list_filter = ('direction', 'file_extension', 'created_at')
    search_fields = ('original_text', 'translated_text', 'file_name')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    def original_text_short(self, obj):
        return obj.original_text[:50] + '...' if len(obj.original_text) > 50 else obj.original_text
    original_text_short.short_description = 'Original Text'

    def translated_text_short(self, obj):
        return obj.translated_text[:50] + '...' if len(obj.translated_text) > 50 else obj.translated_text
    translated_text_short.short_description = 'Translated Text'

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_preview', 'position', 'views', 'active', 'created_at')
    list_filter = ('position', 'active', 'created_at')
    search_fields = ('title', 'content')

    def media_preview(self, obj):
        if obj.media_file and obj.media_type == 'image':
            return format_html('<img src="{}" style="max-height: 50px;" />', obj.media_file.url)
        elif obj.media_file and obj.media_type == 'video':
            return format_html('<video src="{}" style="max-height: 50px;" controls></video>', obj.media_file.url)
        return "No media"
    media_preview.short_description = 'Media Preview'



@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('first_name', 'last_name', 'email', 'phone')

admin.site.register(TranslationHistory, TranslationHistoryAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)
