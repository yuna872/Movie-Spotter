import heapq, math, random
from dateutil.relativedelta import relativedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieSerializer, ReviewSerializer, ReviewListSerializer
from .models import Movie, Review
from django.contrib.auth import get_user_model

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
        serializer = ReviewListSerializer(review_list, many=True)
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

    # 팔로잉한 유저별
    for following in my_followings:
        same_cnt = 0                    # 좋아하는 영화가 겹치는 수
        not_same_movies = []            # 팔로잉 유저는 좋아요를 눌렀지만, 나는 좋아요를 누르지 않은 영화를 담는 리스트
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
                # 리스트에 추가
                not_same_movies.append(following_like_movie)
        
        # 겹치는 좋아요 수가 많은 순으로
        # 팔로잉 유저가 좋아요 누른 영화들 중 나는 좋아요를 누르지 않은 영화를 정렬 
        tmp = (-same_cnt, not_same_movies)
        following_tier_movie_list.append(tmp)
        heapq.heappush(following_tier_movie_list, tmp)
    # following_tier_movie_list.sort()

    result = []
    # 1티어 팔로잉 유저부터
    for tier in following_tier_movie_list:
        for movie in tier[1]:
            # 중복 제거
            if movie.pk not in result:
                result.append(movie.pk)
            # 20개면 종료
            if len(result) == 20:
                break
        
        if len(result) == 20:
            break

    # Response
    recommend = []
    for movie_pk in result:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        recommend.append(serializer.data)
    return Response(recommend)    
    

@api_view(['POST'])
def recommendbymylikes(request):
    # 내가 좋아요 한 영화들, 총 장르 비율 해시 구하기
    my_genre_rate = {}
    me = get_object_or_404(get_user_model(), pk=request.data['user_id'])
    my_like_movies = me.like_movies.all()        # 내가 좋아요 누른 영화객체를 담은 리스트
    all_movies = Movie.objects.all()             # 모든 영화 객체 리스트
             
    # 좋아요한 영화가 없는 경우 랜덤 추천
    if len(my_like_movies) == 0:
        movie_sub = []
        
        for movie in all_movies:
            if movie.vote_average >= 6:         # 평균 평점이 6점 이상이면서
                if movie.vote_count >= 10000:   # 투표수가 10000이상인 영화 중
                    movie_sub.append(movie.pk)

        random.shuffle(movie_sub)
        recommend = []     
        for movie_pk in movie_sub[:20]:         # 랜덤 2개 추천
            movie = get_object_or_404(Movie, pk=movie_pk)
            serializer = MovieSerializer(movie)
            recommend.append(serializer.data)
        return Response(recommend)


    # 좋아요한 영화가 1개 이상인 경우
    for movie in my_like_movies:
        # 장르 개수 구하기
        genre = movie.genres.all()
        for g in genre:
            tmp = g.id
            if tmp not in my_genre_rate:
                my_genre_rate[tmp] = 1
            else:
                my_genre_rate[tmp] += 1
    # 비율 계산
    # 20개 이상에 가깝게, 비율에 따른 장르별 영화 할당량 값을 계산
    tmp = 20/sum(my_genre_rate.values())
    for key in my_genre_rate:
        my_genre_rate[key] = math.ceil(my_genre_rate[key]*tmp)

    my_like_movies_id = []                  
    for movie in my_like_movies:            # 내가 좋아요 누른 영화 pk를 담은 리스트
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

    
    movie_sub = []                      # 조건에 부합하는 영화 pk를 담은 리스트
    for movie in all_movies:
        # 평균 평점 - 2점보다 높고,
        if movie.vote_average >= my_vote_average_avg - 2:
            # 투표수 평균이 0.5배이상 1.5배 이하인 경우
            if my_vote_count_avg*0.5 <= movie.vote_count <= my_vote_count_avg*1.5:
                movie_sub.append(movie.pk)
    
    # 비슷한 영화들 중 매번 새로운 추천을 위해 셔플
    random.shuffle(movie_sub)

    result = []      # 추천할 영화 pk를 담은 리스트
    for movie_pk in movie_sub:
        movie = get_object_or_404(Movie, pk=movie_pk)
        # 영화 장르 중
        for genre in movie.genres.all():
            # 하나라도 장르 비율 해시에 부합하고,
            if genre.id in my_genre_rate:
                # 내가 좋아요를 누른 영화가 아니면,
                if movie.pk not in my_like_movies_id:
                    result.append(movie.pk)
                my_genre_rate[genre.id] -= 1
                # 장르 할당량을 모두 추천했으면
                if my_genre_rate[genre.id] == 0:
                    # 해당 장르 pop
                    my_genre_rate.pop(genre.id)
                break

        # 모든 장르 할당량을 추천했으면,
        if len(my_genre_rate) == 0:
            # Response
            recommend = []     
            for movie_pk in result:
                movie = get_object_or_404(Movie, pk=movie_pk)
                serializer = MovieSerializer(movie)
                recommend.append(serializer.data)
            return Response(recommend)

    # 모든 영화를 봤지만, 할당량이 남았더라도,
    if len(my_genre_rate) != 0:  
        # Response
        recommend = []     
        for movie_pk in result:
            movie = get_object_or_404(Movie, pk=movie_pk)
            serializer = MovieSerializer(movie)
            recommend.append(serializer.data)
        return Response(recommend)



@api_view(['GET'])
def recommendformainpage(request):
    get_all_movies = Movie.objects.all()
    all_movies = []
    for movie in get_all_movies:
        dic = {}
        dic['id'] = movie.pk
        dic['original_language'] = movie.original_language
        dic['vote_count'] = movie.vote_count
        dic['vote_average'] = movie.vote_average
        dic['release_date'] = movie.release_date
        all_movies.append(dic)

    all_movies_sorted = sorted(all_movies, key=lambda x: x['vote_average'], reverse=True)
    # new_movies
    new_movies_sorted = sorted(all_movies_sorted, key=lambda x: x['release_date'], reverse=True)
    new_movies_sub = new_movies_sorted[:30]
    random.shuffle(new_movies_sub)
    new_movies = []     
    for movie in new_movies_sub[:20]:
        movie = get_object_or_404(Movie, pk=movie['id'])
        serializer = MovieSerializer(movie)
        new_movies.append(serializer.data)

    # korean_movies, international_movies
    korean_movies_sub = []
    international_movies_sub = []
    movie_cnt = 0
    for movie in all_movies_sorted:
        if movie['original_language'] == 'ko':
            if len(korean_movies_sub) < 40:
                korean_movies_sub.append(movie['id'])
                movie_cnt += 1
        else:
            if len(international_movies_sub) < 40:
                international_movies_sub.append(movie['id'])
                movie_cnt += 1
        if movie_cnt == 80:
            break

    random.shuffle(korean_movies_sub)
    random.shuffle(international_movies_sub)
    korean_movies = []   
    international_movies = []  
    for movie_pk in korean_movies_sub[:20]:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        korean_movies.append(serializer.data)
    for movie_pk in international_movies_sub[:20]:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        international_movies.append(serializer.data)


    # new_movies
    hot_movies_sub = []
    hot_movies_sorted = sorted(all_movies_sorted, key=lambda x: x['vote_count'], reverse=True)
    hot_movies_sub = hot_movies_sorted[:30]
    random.shuffle(hot_movies_sub)
    hot_movies = []     
    for movie in hot_movies_sub[:20]:
        movie = get_object_or_404(Movie, pk=movie['id'])
        serializer = MovieSerializer(movie)
        hot_movies.append(serializer.data)

    # Response
    recommend = {}
    recommend['new_movies'] = new_movies
    recommend['korean_movies'] = korean_movies
    recommend['international_movies'] = international_movies
    recommend['hot_movies'] = hot_movies

    return Response(recommend)


@api_view(['POST'])
def similarmovies(request):
    get_all_movies = Movie.objects.all()
    now_movie = get_object_or_404(Movie,title=request.data['title'])
    similar_sub = []
    check_genres = request.data['genres']
    for movie in get_all_movies:
        is_valid = 0
        movie_genres = []
        for genre in movie.genres.all():
            movie_genres.append(genre.pk)
        for check in check_genres:
            if check['id'] in movie_genres:
                is_valid = 1
                break

        if is_valid:
            # 평균 평점이 -1점보다 이상이면서
            if now_movie.vote_average -1 <= movie.vote_average:
                # 투표수 평균이 0.5배이상 1.5배 이하며
                if now_movie.vote_count*0.5 <= movie.vote_count <= now_movie.vote_count*1.5:
                    # 5년 내외의 영화인 경우
                    if now_movie.release_date - relativedelta(years=5) <= movie.release_date <= now_movie.release_date + relativedelta(years=5):
                        if movie.pk != now_movie.pk:
                            similar_sub.append(movie.pk)

    # 10개 이상이면 10개까지 추천
    result = []
    if len(similar_sub) > 10:
        random.shuffle(similar_sub)
        result = similar_sub[:10]
    else:
        random.shuffle(similar_sub)
        result = similar_sub

    # Response
    recommend = []     
    for movie_pk in result:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        recommend.append(serializer.data)

    return Response(recommend)

@api_view(['GET'])
def firstmodal(request):
    get_all_movies = Movie.objects.all()
    all_movies = []
    for movie in get_all_movies:
        dic = {}
        dic['id'] = movie.pk
        dic['original_language'] = movie.original_language
        dic['vote_count'] = movie.vote_count
        dic['vote_average'] = movie.vote_average
        dic['release_date'] = movie.release_date
        all_movies.append(dic)

    # 평균 평점을 기준으로 내림차순 정렬
    all_movies_sorted = sorted(all_movies, key=lambda x: x['vote_average'], reverse=True)
    movie_sub = []
    random.shuffle(all_movies_sorted)
    for movie in all_movies_sorted:
        # 투표수가 8000이상인 영화
        if movie['vote_count'] >= 8000:
            movie_sub.append(movie['id'])

    # Response
    recommend = [] 
    for movie_pk in movie_sub[:30]:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        recommend.append(serializer.data)

    return Response(recommend)