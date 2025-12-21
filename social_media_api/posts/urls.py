from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, LikePostView, UnlikePostView
from django.urls import path


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

posts_router = NestedDefaultRouter(router, 'posts', lookup='post')
posts_router.register('comments', CommentViewSet, basename='post-comments')

urlpatterns = router.urls + posts_router.urls

urlpatterns += [
    path('feed/', FeedView.as_view(), name='user-feed'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]
