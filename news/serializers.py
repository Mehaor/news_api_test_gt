from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import NewsPiece, NewsGroup


class NewsPieceSerializer(serializers.ModelSerializer):
    shorter_title = serializers.SerializerMethodField('get_shorty_title')

    class Meta:
        model = NewsPiece
        fields = ('id', 'title', 'news_url', 'shorter_title')

    def get_shorty_title(self, obj):
        if obj.news_url and len(obj.news_url) > 10:
            return obj.title[0:10]
        return obj.title


class NewsGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsGroup
        fields = ('name', 'news')
