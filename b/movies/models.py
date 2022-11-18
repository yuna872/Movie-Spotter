from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    original_language = models.CharField(max_length=128)
    adult = models.BooleanField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    release_date = models.DateField()
    poster_path = models.CharField(max_length=128)
    backdrop_path = models.CharField(max_length=128)
    genres = models.ManyToManyField(Genre, related_name='movie_genres')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    rank = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')