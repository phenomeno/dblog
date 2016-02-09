from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    post_title = models.CharField(max_length=255)
    post_body = models.TextField()
    post_category = models.CharField(max_length=127)
    written_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_title

    def was_published_recently(self):
        return self.written_date >= timezone.now() - datetime.timedelta(days=1)

    @property
    def slug(self):
        return slugify(self.post_title)
