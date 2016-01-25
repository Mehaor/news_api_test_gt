from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'news-pieces', views.NewsPieceViewSet)
router.register(r'news-groups', views.NewsGroupViewSet)

