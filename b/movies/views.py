import heapq, math, random
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
  else:
      me.like_reviews.add(review.pk)
      is_like = True
  
  return Response(is_like)



@api_view(['POST'])
def recommendbymyfollowings(request):
    # by followings
    me = get_object_or_404(get_user_model(), pk=request.data['user_id'])
    my_followings = me.followings.all()
    my_like_movies = me.like_movies.all()

    following_tier_movie_list = []
    # 팔로잉 유저별
    for following in my_followings:
        # 좋아하는 영화가 겹치는 수
        same_cnt = 0
        # 팔로잉 유저는 좋아요를 눌렀지만, 나는 좋아요를 누르지 않은 영화를 담는 리스트
        not_same_movies = []
        following_like_movies = following.like_movies.all()
        # 팔로잉 유저가 좋아요를 누른 영화들 중
        for following_like_movie in following_like_movies:
            # 내가 좋아요를 누른 영화들과 같은 게 있나요?
            is_same = 0
            for my_like_movie in my_like_movies:
                # 있다면
                if following_like_movie.id == my_like_movie.id:
                    is_same = 1
                    break
            # 겹치는 수 + 1
            if is_same:
                same_cnt += 1
            # 없다면, 
            else:
                not_same_movies.append(following_like_movie)
        
        # 겹치는 좋아요 수가 큰 순으로
        # 팔로잉 유저가 좋아요 누른 영화들 중 나는 좋아요를 누르지 않은 영화를 정렬 
        tmp = (-same_cnt, not_same_movies)
        following_tier_movie_list.append(tmp)
        heapq.heappush(following_tier_movie_list, tmp)
    # following_tier_movie_list.sort()

    result = []
    for tier in following_tier_movie_list:
        for movie in tier[1]:
            if movie.pk not in result:
                result.append(movie.pk)
            
            if len(result) == 20:
                break
        
        if len(result) == 20:
            break

    recommend = []
    for movie_pk in result:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        recommend.append(serializer.data)
    return Response(recommend)    
    

@api_view(['POST'])
def recommendbymylikes(request):
    # 내가 좋아요 한 영화들의 장르 비율 해시를 구하는 함수
    my_genre_rate = {}
    me = get_object_or_404(get_user_model(), pk=request.data['user_id'])
    my_like_movie = me.like_movies.all()
    
    
    # 좋아하는 영화별
    for movie in my_like_movie:
        # 장르별 개수 구하기
        genre = movie.genres.all()
        for g in genre:
            tmp = g.id
            if tmp not in my_genre_rate:
                my_genre_rate[tmp] = 1
            else:
                my_genre_rate[tmp] += 1
    # 비율 계산
    tmp = 20/sum(my_genre_rate.values())
    print(my_genre_rate)
    for key in my_genre_rate:
        my_genre_rate[key] = math.ceil(my_genre_rate[key]*tmp)

    
    # 장르를 포함하는 영화들을 반환하는 함수
    all_movies = Movie.objects.all()
    my_like_movies = me.like_movies.all()
    my_like_movies_id = []
    for movie in my_like_movies:
        my_like_movies_id.append(movie.pk)


    my_vote_count_avg = 0
    my_vote_average_avg = 0

    for movie in my_like_movies:
        my_vote_count_avg += movie.vote_count
        my_vote_average_avg += movie.vote_average
    # 내가 좋아요한 영화들의 투표수 평균
    my_vote_count_avg /= len(my_like_movies)
    # 내가 좋아요한 영화들의 평점 평균
    my_vote_average_avg /= len(my_like_movies)

    result = []
    movie_sub = []
    # 평점들의 평균, 투표수의 평균
    for movie in all_movies:
        if movie.vote_average >= my_vote_average_avg - 2:
            if my_vote_count_avg*0.5 <= movie.vote_count <= my_vote_count_avg*1.5:
                movie_sub.append(movie.pk)
    random.shuffle(movie_sub)
    for movie_pk in movie_sub:
        movie = get_object_or_404(Movie, pk=movie_pk)
        for genre in movie.genres.all():
            if genre.id in my_genre_rate:
                if movie.pk not in my_like_movies_id:
                    result.append(movie.pk)
                my_genre_rate[genre.id] -= 1
                if my_genre_rate[genre.id] == 0:
                    my_genre_rate.pop(genre.id)
                break

        if len(my_genre_rate) == 0:
            recommend = []     
            for movie_pk in result:
                movie = get_object_or_404(Movie, pk=movie_pk)
                serializer = MovieSerializer(movie)
                recommend.append(serializer.data)
            return Response(recommend)

    if len(my_genre_rate) != 0:  
        recommend = []     
        for movie_pk in result:
            movie = get_object_or_404(Movie, pk=movie_pk)
            serializer = MovieSerializer(movie)
            recommend.append(serializer.data)
                
                
            
    



# @api_view(['POST'])
# def recommendbymyfollowings(request):
#     me = get_object_or_404(get_user_model(), pk=request.data['user_id'])
#     my_followings = me.followings.all()
#     my_like_movies = me.like_movies.all()

#     recommend_movie = []
#     max_cnt = 0
#     # 팔로잉 유저별
#     for following in my_followings:
#         # 좋아하는 영화가 겹치는 수
#         same_cnt = 0
#         # 팔로잉 유저는 좋아요를 눌렀지만, 나는 좋아요를 누르지 않은 영화를 담는 리스트
#         not_same_movies = []
#         following_like_movies = following.like_movies.all()
#         # 팔로잉 유저가 좋아요를 누른 영화들 중
#         for following_like_movie in following_like_movies:
#             # 내가 좋아요를 누른 영화들과 같은 게 있나요?
#             is_same = 0
#             for my_like_movie in my_like_movies:
#                 # 있다면
#                 if following_like_movie.id == my_like_movie.id:
#                     is_same = 1
#             # 겹치는 수 + 1
#             if is_same:
#                 same_cnt += 1
#             # 없다면, 
#             else:
#                 not_same_movies.append(following_like_movie)
        
#         # 겹치는 좋아요 수가 최댓값인 팔로잉 유저가 좋아요 누른 영화들중
#         if same_cnt > max_cnt:
#             max_cnt = same_cnt
#             # 나는 좋아요를 누르지 않은 영화를 추천!
#             recommend_movie = not_same_movies

#     result = []     
#     for movie in recommend_movie:
#         movie = get_object_or_404(Movie, pk=movie.pk)
#         serializer = MovieSerializer(movie)
#         result.append(serializer.data)
    
#     return Response(result)