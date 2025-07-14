from django.urls import path

from . import views


urlpatterns = [
    path('users/', views.UserListAPIView.as_view()),
    path('users/<int:pk>/', views.UserRetrieveAPIView.as_view()),
    path('users/<int:pk>/follow', views.follow_user),
    path('users/<int:pk>/posts', views.UserPostListAPIView.as_view()),
    path('register/', views.Register.as_view()),
    path('profile/', views.Profile.as_view())
]
