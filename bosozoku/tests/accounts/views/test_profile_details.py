import random
from os.path import join

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse

from bosozoku.accounts.models import Profile
from bosozoku.events.models import Event
from tests.base.tests import BosozokuTestCase


class ProfileDetailsTest(BosozokuTestCase):
    def test_getDetails_whenLoggedInUserWithNoEvents_shouldGetDetailsWithNoEvents(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertListEmpty(list(response.context['events']))
        self.assertEqual(self.user.id, response.context['profile'].user_id)

    def test_getDetails_whenLoggedInUserWithEvents_shouldGetDetailsWithEvents(self):
        event = Event.objects.create(
            name='TestEvent',
            date='2018-11-20T15:58:44.767594-06:00',
            description='Test event description',
            location='Sofia',
            image='path/to/image.png',
            user=self.user,
        )

        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user.id, response.context['profile'].user_id)
        self.assertListEqual([event], list(response.context['events']))

    def test_postDetails_whenUserLoggedInWithoutImage_shouldChangeImage(self):
        path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'test_event_image.jpg')

        file_name = f'{random.randint(1, 10000)}-test_event_image.jpg'
        file = SimpleUploadedFile(
            name=file_name,
            content=open(path_to_image, 'rb').read(),
            content_type='image/jpeg')

        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            'profile_image': file,
        })

        self.assertEqual(302, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)
        self.assertTrue(str(profile.profile_image).endswith(file_name))

    def test_postDetails_whenUserLoggedInWithImage_shouldChangeImage(self):
        path_to_image = 'path/to/image.png'
        profile = Profile.objects.get(pk=self.user.id)
        profile.profile_image = path_to_image + 'old'
        profile.save()

        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            'profile_image': path_to_image,
        })

        self.assertEqual(302, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)

        # self.assertEqual(path_to_image, str(profile.profile_image.url))
