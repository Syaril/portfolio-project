from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField(default='This is blog post.')
    image = models.ImageField()
    is_important = models.BooleanField(default=False)
