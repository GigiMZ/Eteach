from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostListCreateAPIView.as_view()),
    path('posts/<int:pk>', views.PostRetrieveUpdateDestroyAPIView.as_view()),
    path('comments/', views.CommentListCreateAPIView.as_view()),
    path('comments/<int:pk>', views.CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('tags/', views.TagListCreateAPIView.as_view()),
    path('tags/<int:pk>', views.TagRetrieveUpdateDestroyAPIView.as_view())
]
