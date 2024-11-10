from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Tip

class TipAdmin(admin.ModelAdmin):
    list_display = ('author', 'display_date', 'content', 'delete_button')
    actions = ['delete_all_tips']

    def display_date(self, obj):
        return obj.created.strftime('%Y-%m-%d')
    display_date.short_description = 'Date'

    def delete_button(self, obj):
        delete_url = reverse('admin:ex_tip_delete', args=[obj.pk])
        return format_html(
            '<a href="{url}" class="button" onclick="return confirm(\'Are you sure?\');">❌</a>',
            url=delete_url
        )
    delete_button.short_description = 'Delete'

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def delete_all_tips(self, request, queryset):
        queryset.delete()
    delete_all_tips.short_description = 'Delete selected tips'

admin.site.register(Tip, TipAdmin)
