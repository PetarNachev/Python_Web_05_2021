from django.urls import reverse

from bosozoku.events.models import Event, Going
from tests.base.mixins import UserTestUtils, EventTestUtils
from tests.base.tests import BosozokuTestCase


class GoingEventViewTests(EventTestUtils, UserTestUtils, BosozokuTestCase):
    def test_goingEvent__whenEventNotGoing_shouldCreateGoing(self):
        self.client.force_login(self.user)
        event_user = self.create_user(email='anonymoustest@test.com', password='12345qwe')
        event = self.create_event(
            name='TestEvent',
            date='2018-11-20T15:58:44.767594-06:00',
            description='Test event description',
            location='Sofia',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.post(reverse('going event', kwargs={
            'pk': event.id,
        }))

        self.assertEqual(302, response.status_code)

        going_exists = Going.objects.filter(
            event_id=event.id,
            user_id=self.user.id,
        ) \
            .exists()

        self.assertTrue(going_exists)

    def test_goingEvent__whenEventAlreadyGoing_shouldDeleteTheGoing(self):
        self.client.force_login(self.user)
        event_user = self.create_user(email='anonymoustest@test.com', password='12345qwe')
        event = self.create_event_with__going(
            going_user=self.user,
            name='TestEvent',
            date='2018-11-20T15:58:44.767594-06:00',
            description='Test event description',
            location='Sofia',
            image='path/to/image.png',
            user=event_user,
        )

        response = self.client.post(reverse('going event', kwargs={
            'pk': event.id,
        }))

        self.assertEqual(302, response.status_code)

        going_exists = Going.objects.filter(
            event_id=event.id,
            user_id=self.user.id,

        ) \
            .exists()

        self.assertFalse(going_exists)
