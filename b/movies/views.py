
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.permissions import IsAuthenticated


from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieSerializer, ReviewSerializer
from .models import Movie, Review
from django.contrib.auth import get_user_model
from django.http import HttpResponse 

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET','POST'])
def reviews(request, movie_pk):
    # 리뷰 조회
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        reviews = movie.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    else:
        # 리뷰 create
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = get_object_or_404(get_user_model(), pk=request.data['user_id'])
        # 닉네임 데이터 추가
        request.data['writer'] = user.nickname
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# 내가 쓴 리뷰들을 반환하는 함수
@api_view(['GET'])
def my_reviews(request, user_pk):
    if request.method == 'GET':
        review_list = Review.objects.all().filter(user_id=user_pk)
        serializer = ReviewSerializer(review_list, many=True)
        return Response(serializer.data)


@api_view(['POST'])
# title=movie_title로 해야하나?
def movie_likes(request, movie_pk):
  movie = get_object_or_404(Movie, pk=movie_pk)
  me = get_object_or_404(get_user_model(), pk=request.data['user_id'])
  if me.like_movies.filter(pk=movie.pk).exists():
      me.like_movies.remove(movie.pk)
      is_like = False 
  else:
      me.like_movies.add(movie.pk)
      is_like = True
  
  return Response(is_like)


@api_view(['POST'])
def review_likes(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  me = get_object_or_404(get_user_model(), pk=request.data['user_id'])
  if me.like_reviews.filter(pk=review.pk).exists():
      me.like_reviews.remove(review.pk)
      is_like = False
      ['id']
  else:
      me.like_reviews.add(review.pk)
      is_like = True
  
  return Response(is_like)



@api_view(['POST'])
def recommend(request):
    # 내가 좋아요 한 영화들의 장르 비율 해시를 구하는 함수
    me = get_object_or_404(get_user_model(), pk=request.data['user_id'])
    my_genre_rate = {}
    my_like_movie = me.like_movies.all()
    total_my_like_movie = 0
    
    # 좋아하는 영화별
    for movie in my_like_movie:
        # 장르별 개수 구하기
        for g in movie.genres.all():
            total_my_like_movie += 1
            tmp = g.id
            if tmp not in my_genre_rate:
                my_genre_rate[tmp] = 1
            else:
                my_genre_rate[tmp] += 1
    # 비율 계산
    for i in my_genre_rate:
        my_genre_rate[i] = round(my_genre_rate[i]/total_my_like_movie,2)

    result = []
    # 비율이 높은 3개의 장르를 반환
    for key,value in sorted(my_genre_rate.items(), key=lambda x: x[1], reverse=True)[:3]:
        result.append(key)
    
    # 3개의 장르를 포함하는 영화들을 반환하는 함수
    recommend_movie = []
    all_movies = Movie.objects.all()

    for movie in all_movies:
        genres = movie.genres.all()
        is_valid = 1

        genre_set = []
        for g in genres:
            genre_set.append(g.id)

        for check in result:
            if check not in genre_set:
                is_valid = 0
                break
        
        if is_valid:
            movie = get_object_or_404(Movie, pk=movie.pk)
            serializer = MovieSerializer(movie)
            recommend_movie.append(serializer.data)

    return Response(recommend_movie)