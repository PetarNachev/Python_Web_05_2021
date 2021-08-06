from django.contrib.auth import get_user_model
from django.db import models

from bosozoku.events.models import Event

UserModel = get_user_model()


class Comment(models.Model):
    text = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
