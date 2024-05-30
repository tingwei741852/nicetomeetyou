from main.models import News
from main.serializers import NewsSerializer
from .crawler import fetch_news
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from django_redis import get_redis_connection
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')

@register_job(scheduler, "interval", id="test1", seconds=30, replace_existing=True)   
def scheduled_fetch_news():
    created_count  = fetch_news()
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "news_group",
        {
            "type": "send_update",
            "update": {"status": "News fetched successfully", "created_count": created_count},
        }
    )
    print("created_count:",created_count)
    return created_count

register_events(scheduler)
scheduler.start()

# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer



@api_view(['GET'])
def trigger_fetch_news(request):
    created_count  = fetch_news()
    return Response({"status": "News fetched successfully","created_count": created_count})

@api_view(['GET'])
def get_focus_news(request):
    cacheCon = get_redis_connection("default")
    focusNews = cacheCon.get('focusNews')
    if focusNews is None:
        print("focusNews 尚未被存取")
        display_news = News.objects.filter(display=True)
        focusNews = NewsSerializer(display_news, many=True).data
        focusNews = json.dumps(focusNews)
        cacheCon.set('focusNews', focusNews)
    else:
        focusNews = json.loads(focusNews)

    return Response({"data": focusNews}, status=200)  

class NewsConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)(
            "news_group",
            self.channel_name
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            "news_group",
            self.channel_name
        )

    def send_update(self, event):
        self.send(text_data=json.dumps(event['update']))