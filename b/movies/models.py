from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=200,null=True, blank=True)
    popularity = models.FloatField()
    role = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    original_language = models.CharField(max_length=200)
    adult = models.BooleanField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    release_date = models.DateField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)
    video = models.CharField(max_length=200)
    actors = models.ManyToManyField(Actor, related_name='movie_actors')
    genres = models.ManyToManyField(Genre, related_name='movie_genres')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

    # heapq 모듈로 객체를 정렬하는 알고리즘에서 사용될,
    # 객체 대소 비교를 위한 매직메서드 추가
    def __lt__(self, other):
        return self.vote_count > other.vote_count
        
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    writer = models.CharField(max_length=200)
    content = models.TextField()
    rank = models.FloatField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')