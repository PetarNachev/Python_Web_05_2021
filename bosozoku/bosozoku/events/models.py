
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Event(models.Model):
    name = models.CharField(
        max_length=30,
     )
    date = models.DateTimeField()
    description = models.TextField()
    location = models.CharField(
        max_length=30,
    )
    image = models.ImageField(
        upload_to='events'
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Going(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
