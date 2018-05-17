from django.db import models

# Create your models here.


class Movielist(models.Model):
    Movie_Id = models.CharField(max_length=30)
    Movie_Name = models.CharField(max_length=100)
    Release_Date = models.DateField(max_length=100)
    Rating = models.CharField(max_length=20)

    class Meta:
        indexes = [
            models.Index(fields=['Movie_Id']),
        ]
        ordering = ["Release_Date"]