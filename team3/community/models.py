from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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
	created_on = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=200)
	text = models.TextField()
	location = models.CharField(max_length=200)
	guests = models.ManyToManyField(User)
	
	def __unicode__(self):
		return self.title
	
	@property
	def guestlist(self):
		# watch for large querysets!
		return list(self.guests.all())
		
class Community(models.Model):
	title = models.CharField(max_length=200)
	#users = models.ManyToManyField(User)
	description = models.TextField()
	#posts = models.ManyToManyField(Post, related_name='posts')
	#events = models.ManyToManyField(Event, related_name='events')
	
	def __unicode__(self):
		return self.title