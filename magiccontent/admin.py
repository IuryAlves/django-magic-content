from django.contrib import admin

from .models import Area, Widget, SiteLink


class WidgetAdmin(admin.ModelAdmin):
    list_display = ['name', 'widget_type', 'style_template']


admin.site.register(Widget, WidgetAdmin)
admin.site.register(Area)
admin.site.register(SiteLink)
