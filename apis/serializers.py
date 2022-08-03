from rest_framework import serializers

from homepage.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'bio', 'youtube_url', 'instagram_url',
                  'spotify_url', 'bandcamp_url', 'image',
                  'image_url', 'active', ]