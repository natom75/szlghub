from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png', upload_to='profile_pics')
	desc = models.TextField(max_length=512, default='null')
	year_in_school = models.IntegerField(range(8, 12), default='1')
	class_in_school = models.TextField(max_length=1, default='F')
	points = models.IntegerField(default='0')

	def __str__(self):
		return f'{self.user.username} Profile'
