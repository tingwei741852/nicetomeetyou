from rest_framework import serializers
from main.models import News


class NewsSerializer(serializers.ModelSerializer):
    published_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    class Meta:
        model = News
        fields = '__all__'