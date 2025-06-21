from django.urls import path
from . import views
from post import views as post_views


urlpatterns = [
    path('users/', views.UserListCreateAPIView.as_view()),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroyAPIView.as_view()),
    path('users/<int:pk>/follow', views.follow_user),
    path('users/<int:pk>/posts', views.UserPostListAPIView.as_view()),
    path('users/<int:user_pk>/posts/<int:pk>/', post_views.PostRetrieveUpdateDestroyAPIView.as_view()),
]
