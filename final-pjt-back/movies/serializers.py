from rest_framework import serializers
from .models import Movie, Review



class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user',)


class MovieSerializer(serializers.ModelSerializer):
    # review_set = ReviewSerializer(many=True, read_only=True)
    # review_count = serializers.IntegerField(source='review_set.count', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_users',)



