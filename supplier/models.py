from django.db import models
from django.contrib.auth.models import User


class Shop(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length = 30, blank=False, unique=True)
	location = models.CharField(max_length = 30, blank=False)
	desc = models.CharField(max_length=250, blank=False)

	def __str__(self):
		return self.name

# Create your models here.
