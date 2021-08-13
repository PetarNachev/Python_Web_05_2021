from django.contrib.auth import get_user_model

from bosozoku.events.models import Event, Going

UserModel = get_user_model()


class EventTestUtils:

    def create_event(self, **kwargs):
        return Event.objects.create(**kwargs)

    def create_event_with__going(self, going_user, **kwargs):
        event = self.create_event(**kwargs)
        Going.objects.create(
            event=event,
            user=going_user,
        )
        return event


class UserTestUtils:
    def create_user(self, **kwargs):
        return UserModel.objects.create_user(**kwargs)
