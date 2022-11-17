
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieSerializer, ReviewSerializer
from .models import Movie, Review
from django.contrib.auth import get_user_model



@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = MovieSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         # serializer.save()
    #         serializer.save(user=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    
    # elif request.method == 'DELETE':
    #     movie.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # elif request.method == 'PUT':
    #     serializer = MovieSerializer(movie, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)


@api_view(['GET','POST'])
def reviews(request, movie_pk):
    # 리뷰 조회
    if request.method == 'GET':
        reviews = get_list_or_404(Review, pk=movie_pk)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    # 리뷰 create
    else:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        # request.data._mutable = True
        # request.data['movie'] = "example@mail.com"
        # request.data._mutable = False
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    # 삭제 및 수정 기능
    # 로그인이 상태며
    if request.user.is_authenticated:
        # 리뷰를 쓴 사람이면
        if request.user == review.user:
            if request.method == 'DELETE':
                review.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

            elif request.method == 'PUT':
                serializer = ReviewSerializer(review, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)

        else:
            print('')
            # 작성자만 수정할 수 있습니다.
    else:
        print('')
        # 로그인을 해주세요
        

# 내가 쓴 리뷰들을 반환하는 함수
@api_view(['GET'])
def my_reviews(request, my_pk):
    if request.method == 'GET':
        review_list = Review.objects.all().filter(user_id=my_pk)
        serializer = ReviewSerializer(review_list, many=True)
        return Response(serializer.data)






# @require_POST
# def likes(request, article_pk):
#     if request.user.is_authenticated:
#         article = Article.objects.get(pk=article_pk)

#         # 좋아요 추가할지 취소할지 무슨 기준으로 if문을 작성할까?
#         # 현재 게시글에 좋아요를 누른 유저 목록에 현재 좋아요를 요청하는 유저가 있는지 없는지를 확인
#         # if request.user in article.like_users.all():
        
#         # 현재 게시글에 좋아요를 누른 유저중에 현재 좋아요를 요청하는 유저를 검색해서 존재하는지를 확인 
#         if article.like_users.filter(pk=request.user.pk).exists():
#             # 좋아요 취소 (remove)
#             article.like_users.remove(request.user)
#         else:
#             # 좋아요 추가 (add)
#             article.like_users.add(request.user)
#         return redirect('articles:index')
#     return redirect('accounts:login')
    

@api_view(['POST'])
# title=movie_title로 해야하나?
def movie_like(request, my_pk, movie_pk):
  movie = get_object_or_404(Movie, pk=movie_pk)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_movies.filter(pk=movie.pk).exists():
      me.like_movies.remove(movie.pk)
      is_like = False
      
  else:
      me.like_movies.add(movie.pk)
      is_like = True
  
  return Response(is_like)

@api_view(['POST'])
def review_like(request, my_pk, review_pk):
  review = get_object_or_404(Movie, pk=review_pk)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_reviews.filter(pk=review.pk).exists():
      me.like_reviews.remove(review.pk)
      is_like = False
      
  else:
      me.like_reviews.add(review.pk)
      is_like = True
  
  return Response(is_like)

# Response로 True or False를 보내는게 맞는지? 고민