from django import forms

from bosozoku.common.models import Comment
from bosozoku.events.models import Event


class CommentForm(forms.ModelForm):
    event_pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Comment
        fields = ('text', 'event_pk')

    def save(self, commit=True):
        event_pk = self.cleaned_data['event_pk']
        event = Event.objects.get(pk=event_pk)
        comment = Comment(
            text=self.cleaned_data['text'],
            event=event,
        )

        if commit:
            comment.save()

        return comment
