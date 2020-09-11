from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .routers import GetPostOnlyRouter
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>[0-9]+)/comments',
                CommentViewSet,
                basename='comments')

get_post_router = GetPostOnlyRouter()
get_post_router.register(r'group', GroupViewSet, basename='group')
get_post_router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(get_post_router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
