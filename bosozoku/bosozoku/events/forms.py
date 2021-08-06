import os
from os.path import join

from django import forms
from django.conf import settings

from core.forms import BoostrapFormMixin
from bosozoku.events.models import Event


class EventForm(BoostrapFormMixin, forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('user', )


class EditEventForm(EventForm):

    def save(self, commit=True):
        db_event = Event.objects.get(pk=self.instance.id)
        if commit:
            os.remove(join(settings.MEDIA_ROOT, str(db_event.image)))
        return super().save(commit)

    class Meta:
        model = Event
        fields = '__all__'

