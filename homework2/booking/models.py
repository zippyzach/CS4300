from django.db import models

class Movie(models.Model)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    duration = models.DurationField()
    
    def __str__(self):
        return self.title