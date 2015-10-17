from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Community(models.Model):
	users
	description = models.TextField()
	posts = models.ManyToManyField("self")
	events

class Post(models.Model):
	author = models.ForeignKey(User)
	created_on = models.DateTimeField(auto_now_add=True)
	text = models.TextField()
	
	def __unicode__(self):
		return self.text


class Comment(models.Model):
	author = models.ForeignKey(User)
	post = models.ForeignKey(Post)
	created_on = models.DateTimeField(auto_now_add=True)
	text = models.TextField()
	
	def __unicode__(self):
		return self.text
	
class Event(models.Model):
	author = models.ForeignKey(User)
	created_on = models.DateTimeField(auto_now_add=True)
	text = models.TextField()
	location = models.CharField(max_length=200)
	guests = models.ManyToManyField("self")
	
	@property
	def guestlist(self):
		# watch for large querysets!
		return list(self.guests.all())