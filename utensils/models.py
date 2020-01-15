from django.db import models
from django.urls import reverse

class Utensils(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    img = models.CharField(max_length=120)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])