from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=160)
    description = models.TextField(max_length=160)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Image',) # height_field=100, width_field=100

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
