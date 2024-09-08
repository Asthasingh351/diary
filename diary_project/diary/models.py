from django.db import models
from django.contrib.auth.models import User

class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.title} ({self.date})'

