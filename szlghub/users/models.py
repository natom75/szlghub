from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png', upload_to='profile_pics')
	desc = models.TextField(max_length=512, default='null')
	points = models.IntegerField(default='0')
	SEMESTER_CHOICES = ( 
	("NY", "NY"),
    ("9", "9"), 
    ("10", "10"), 
    ("11", "11"), 
    ("12", "12")
	) 
	year_in_school = models.CharField( 
        max_length = 20, 
        choices = SEMESTER_CHOICES, 
        default = '0'
        ) 
	CLASS_CHOICES = ( 
	("A", "A"),
    ("B", "B"), 
    ("C", "C"), 
    ("D", "D"), 
    ("E", "E"), 
    ("F", "F")
	) 
	class_in_school = models.CharField( 
        max_length = 20, 
        choices = CLASS_CHOICES, 
        default = 'A'
        ) 

	def __str__(self):
		return f'{self.user.username} Profile'
