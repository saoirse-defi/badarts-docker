from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ArtistSerializer
from homepage.models import Artist

#class ArtistAPIViewset(viewsets.ModelViewSet):
 #   queryset = ArtistSerializer.objects.all()
#
 #   serializer_class = ArtistSerializer


@api_view(['GET', ])
def api_artist_view(request, artist_id):
    try:
        artist = Artist.objects.get(pk=artist_id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)