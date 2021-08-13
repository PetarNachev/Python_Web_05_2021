from django.urls import reverse

from bosozoku.events.models import Event, Going
from tests.base.mixins import EventTestUtils, UserTestUtils
from tests.base.tests import BosozokuTestCase


class EventDetailsTest(EventTestUtils, UserTestUtils, BosozokuTestCase):

    def test_getEventDetails_whenEventExistsAndIsCreator_shouldReturnDetailsForCreator(self):
        self.client.force_login(self.user)
        event = self.create_event(
            name='TestEvent',
            date='2018-11-20T15:58:44.767594-06:00',
            description='Test event description',
            location='Sofia',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.get(reverse('event details', kwargs={
            'pk': event.id,
        }))

        self.assertTrue(response.context['is_creator'])
        self.assertFalse(response.context['is_going'])

    def test_getEventDetails_whenEventExistsAndIsNotCreatorAndNotGoing_shouldReturnDetailsForCreator(self):
        self.client.force_login(self.user)
        event_user = self.create_user(email='event@user.com', password='12345qwe')
        event = self.create_event(
            name='TestEvent',
            date='2018-11-20T15:58:44.767594-06:00',
            description='Test event description',
            location='Sofia',
            image='path/to/image.png',
            user=event_user,
        )

        response = self.client.get(reverse('event details', kwargs={
            'pk': event.id,
        }))

        self.assertFalse(response.context['is_creator'])
        self.assertFalse(response.context['is_going'])

    def test_getEventDetails_whenEventExistsAndIsNotCreatorAndGoing_shouldReturnDetailsForCreator(self):
        self.client.force_login(self.user)
        event_user = self.create_user(email='event@user.com', password='12345qwe')
        event = self.create_event_with__going(
            going_user=self.user,
            name='TestEvent',
            date='2018-11-20T15:58:44.767594-06:00',
            description='Test event description',
            location='Sofia',
            image='path/to/image.png',
            user=event_user,
        )

        response = self.client.get(reverse('event details', kwargs={
            'pk': event.id,
        }))

        self.assertFalse(response.context['is_creator'])
        self.assertTrue(response.context['is_going'])
