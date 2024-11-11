from django.db import models

class Movie(models.Model): 
    GENRE_CHOICE = (
        ('action', 'Action'),
        ('drama', 'Drama'),
        ('comedy', 'Comedy')
    )
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=30)
    release_date = models.DateField()
    genre = models.CharField(max_length=6, choices=GENRE_CHOICE)

    def __str__(self): 
        return self.title