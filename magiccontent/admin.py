from django.contrib import admin

from .models import (Area, Widget, SimpleContent, LongContent, IconContent,
                     BackgroundArea, PageLink, GalleryContent)


class WidgetAdmin(admin.ModelAdmin):
    list_display = ['name', 'widget_type', 'style_template']


admin.site.register(Widget, WidgetAdmin)
admin.site.register(Area)

admin.site.register(SimpleContent)
admin.site.register(LongContent)
admin.site.register(IconContent)
admin.site.register(BackgroundArea)
admin.site.register(PageLink)
admin.site.register(GalleryContent)
