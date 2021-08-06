from django.contrib import admin

from bosozoku.events.models import Event


class EventAdmin(admin.ModelAdmin):

    def going_count(self, obj):
        return obj.going_set.count()


admin.site.register(Event, EventAdmin)
