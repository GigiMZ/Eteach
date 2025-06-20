from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserListCreateAPIView.as_view()),
    path('users/<int:pk>', views.UserRetrieveUpdateDestroyAPIView.as_view()),
    path('users/<int:pk>/follow', views.follow_user),
]
