from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, trigger_fetch_news, get_focus_news

router = DefaultRouter()
router.register(r'news', NewsViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('fetch-news/', trigger_fetch_news, name='fetch-news'),
    path('get_focus_news/', get_focus_news, name='get_focus_news'),
]