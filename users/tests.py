from django.test import TestCase
from users.models import Profile
from django.contrib.auth.models import User
from datetime import datetime
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
filename = '/home/sharon/Documents/Awwards/media/default.jpg'

# Create your tests here.

class TestProfileModel(TestCase):
    def setUp(self):
        self.user = User.objects.get_or_create(username="testuser",password="adminpass")
        profiles = Profile.objects.all()
        for profile in profiles:
            profile.delete()
        self.profile = Profile.objects.get_or_create(
            image=SimpleUploadedFile(name='test_image.jpg', content=open(filename, 'rb').read(), content_type='image/jpeg'),
            user=self.user[0]
        )
        self.profile= self.profile[0]
        
    def test_profile_create(self):
        self.profile.save()
        query = Profile.objects.all()
        self.assertTrue(len(query)>0)
        
    def test_profile_update(self):
        self.profile.save()
        prevImg = self.profile.image.url
        self.profile.image = SimpleUploadedFile(name='test_image.jpg', content=open(updated_filename, 'rb').read(), content_type='image/jpeg')
        self.profile.save()
        updatedImg = self.profile.link
        self.assertNotEqual(prevImg,updatedImg)
        
    def test_delete_profile(self):
        self.profile.save()
        self.profile.delete()
        query =Profile.objects.all()
        self.assertIs(len(query),0)
        
    def test_profile_is_instance(self):
        self.profile.save()
        query = Profile.objects.all()
        self.assertIsInstance(query[0],Profile)
        
    def test_profile_str(self):
        self.profile.save()
        profile = Profile.objects.all()
        self.assertTrue(str(profile[0]),f'{self.profile.user.username} Profile')
