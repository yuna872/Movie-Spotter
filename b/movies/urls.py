# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/reviews/', views.reviews),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('reviews/<int:user_pk>', views.my_reviews),
    path("<int:movie_pk>/moivelikes/", views.movie_likes, name="movie_likes"),
    path("<int:review_pk>/reviewlikes/", views.review_likes, name="review_likes"),
    # # 필수 작성
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]