from django.db import models

class MyWatchlistItem(models.Model):
    watched = models.TextField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()