from django.test import TestCase
from users.models import *

class TestProfiles(TestCase):
	def setUp(self):
		self.user1 = User.objects.create(
			first_name = "Test user",
			last_name = "lastnameUser",
			username = "Mrrac"
			)
		self.profile = Profile.objects.create( 
			user = self.user1,
			balance = 100.0,
			requirements = "Писать код, хорошо работать",
			about = "Люблю лыжи",
			speciality = "Python developer",
			role = "Programmer",
			)
		print('\n\n\x1b[30;42m' + 'models CREATED' + '\x1b[0m')
	def test_slug(self):
		self.assertEqual(self.profile.slug, "mrrac")
		print('\n\n\x1b[30;42m' + 'slug profile PASSED ' + '\x1b[0m')