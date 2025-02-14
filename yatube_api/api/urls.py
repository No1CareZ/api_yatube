from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework import routers

from .views import PostViewSet, CommentViewSet, GroupViewSet


app_names = 'api'

router = routers.DefaultRouter()
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router.register('posts', PostViewSet, basename='posts')
# GET, POST from 'posts/' # GET, PUT, PATCH, DELETE from 'posts/id'
router.register('groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token, name='FUCK YANDEX'),
    path('v1/', include(router.urls)),
]
