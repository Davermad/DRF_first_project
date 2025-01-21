from django.contrib import admin
from .models import Category, Publication


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')
    search_fields = ('name',)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category', 'content', 'is_archived', 'created', 'updated')
    list_filter = ('is_archived', 'category', 'created', 'updated')
    search_fields = ('content', 'user__username', 'category__name')
    ordering = ('-created',)
    readonly_fields = ('created', 'updated')

    fieldsets = (
        (None, {
            'fields': ('user', 'category', 'content', 'image', 'is_archived')
        }),
        ('Техническая информация', {
            'fields': ('created', 'updated'),
        }),
    )
