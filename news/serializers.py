from rest_framework import serializers
from .models import NewsPiece

class NewsPieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPiece
        fields = ('title', 'url')
