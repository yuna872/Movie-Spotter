from rest_framework import serializers
from .models import Movie, Review, Genre, Actor


# Myinfo.vue에서 호출, myreviews.py에서 사용할 serializer
class ReviewListSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'
    movie = MovieSerializer()
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie', 'like_users',)

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie', 'like_users',)

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_users',)



