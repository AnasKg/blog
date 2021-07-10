from django.urls import path, include
from rest_framework import routers
from post.api import views

router = routers.DefaultRouter()

router.register('tags', views.TagViewSet)
router.register('categories', views.CategoryViewSet)
router.register('posts', views.PostViewSet)


urlpatterns = [
    path('v1/', include(router.urls))
]
