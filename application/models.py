from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=200, blank=True)
    thumbnail = models.URLField(max_length=400)
    read_more = models.URLField(max_length=400, blank=True)
    category = models.CharField(max_length=10, blank=True)
    id = models.AutoField(primary_key=True)

    def __str__(self) -> str:
        return self.title
