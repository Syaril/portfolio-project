from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField(default='This is blog post.')
    image = models.ImageField(upload_to='images/')
    is_important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')