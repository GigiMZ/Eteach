from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostListCreateAPIView.as_view()),
    path('posts/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view()),
    path('posts/<int:pk>/vote_up', views.post_up_vote),
    path('posts/<int:pk>/vote_down', views.post_down_vote),
    path('posts/<int:pk>/vote_up_remove', views.post_up_vote_remove),
    path('posts/<int:pk>/vote_down_remove', views.post_down_vote_remove),
    path('posts/<int:pos_pk>/comments', views.CommentListCreateAPIView.as_view()),
    path('posts/<int:pos_pk>/comments/<int:com_pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('posts/<int:pos_pk>/comments/<int:com_pk>/vote_up', views.comment_up_vote),
    path('posts/<int:pos_pk>/comments/<int:com_pk>/vote_down', views.comment_down_vote),
    path('posts/<int:pos_pk>/comments/<int:com_pk>/vote_up_remove', views.comment_up_vote_remove),
    path('posts/<int:pos_pk>/comments/<int:com_pk>/vote_down_remove', views.comment_down_vote_remove),
    path('tags/', views.TagListCreateAPIView.as_view()),
    path('tags/<int:pk>', views.TagRetrieveUpdateDestroyAPIView.as_view())
]
