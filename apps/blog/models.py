from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

class Post(models.Model):
    """ Post model to allow storage of blog posts in db. """

    class Status(models.TextChoices):
        """ subclass to allow writers to save blog posts as draft or published status. """
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    # Use the current date and time as the default value for publish field
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    class Meta:
        """ Posts will be returned in reverse chronological order by default"""
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self) -> str:
        return self.title
