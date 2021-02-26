from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Title: {self.title}"


    def get_absolute_url(self):
        return reverse('blog-post', kwargs={'pk' : self.pk})




class About(models.Model):
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"content {self.content}"


    def get_absolute_url(self):
        return reverse('blog-about', kwargs={'pk' : self.pk})



class Event(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(default='profile_pics/default.png', upload_to='events_pics')
	content = models.TextField()
	date_created = models.DateTimeField(default=timezone.now)
	date_updated = models.DateTimeField(auto_now = True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f"content {self.content}"

	def get_absolute_url(self):
		return reverse('blog-events', kwargs={'pk' : self.pk})

	


class Membership(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"content {self.content}"

    def get_absolute_url(self):
        return reverse('blog-membership', kwargs={'pk' : self.pk})

    
class Contact(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"content {self.content}"

    def get_absolute_url(self):
        return reverse('blog-contact', kwargs={'pk' : self.pk})

    
