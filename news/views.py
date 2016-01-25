from rest_framework import viewsets, permissions
from .models import NewsPiece, NewsGroup
from .serializers import NewsPieceSerializer, NewsGroupSerializer


class NewsPieceViewSet(viewsets.ModelViewSet):
    queryset = NewsPiece.objects.all().order_by('-id')
    serializer_class = NewsPieceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )




class NewsGroupViewSet(viewsets.ModelViewSet):
    queryset = NewsGroup.objects.all()
    serializer_class = NewsGroupSerializer
    permission_classes = (permissions.IsAuthenticated, )


