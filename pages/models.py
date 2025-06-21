from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title