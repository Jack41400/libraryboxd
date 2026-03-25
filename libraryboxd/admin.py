from django.contrib import admin
from django.utils.html import format_html
from .models import Book, ReadingEntry, UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_private', 'created_at', 'updated_at')
    list_filter = ('is_private',)
    search_fields = ('user__username', 'user__email')
    filter_horizontal = ('favorite_books',)

class ReadingEntryInline(admin.TabularInline):
    model = ReadingEntry
    extra = 0
    fields = ('user', 'rating', 'date_read', 'is_active', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'publication_year',
        'isbn',
        'library_code',
        'entry_count',
        'created_at',
    )
    list_filter = ('publication_year',)
    search_fields = ('title', 'author', 'isbn', 'library_code')
    inlines = [ReadingEntryInline]

    # For non-technical admins, grouping fields into sections helps
    fieldsets = (
        ("Basic info", {
            'fields': ('title', 'author', 'publication_year', 'isbn')
        }),
        ("Description & cover", {
            'fields': ('description', 'cover_image_url'),
            'classes': ('collapse',)
        }),
        ("Library metadata", {
            'fields': ('library_code',),
            'classes': ('collapse',)
        }),
        ("Timestamps", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

    def entry_count(self, obj):
        return obj.reading_entries.count()
    entry_count.short_description = "Reading entries"

@admin.register(ReadingEntry)
class ReadingEntryAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'book',
        'rating',
        'date_read',
        'visibility',
        'is_active',
        'short_review',
        'created_at',
    )
    list_filter = (
        'rating',
        'visibility',
        'is_active',
        'date_read',
        'created_at',
    )
    search_fields = (
        'user__username',
        'user__email',
        'book__title',
        'book__author',
        'review',
    )
    date_hierarchy = 'date_read'
    autocomplete_fields = ('user', 'book')

    fieldsets = (
        ("Entry details", {
            'fields': ('user', 'book', 'date_read', 'rating', 'review')
        }),
        ("Visibility & status", {
            'fields': ('visibility', 'is_active'),
        }),
        ("Timestamps", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

    def short_review(self, obj):
        if not obj.review:
            return ""
        # Limit length for list_display
        text = obj.review
        if len(text) > 60:
            text = text[:57] + "..."
        return text
    short_review.short_description = "Review (short)"