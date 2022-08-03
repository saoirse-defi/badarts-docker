import uuid
from django.db import models

from homepage.models import Artist


class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=254)
    artists = models.ManyToManyField(Artist)
    thumbnail_url = models.CharField(max_length=254, null=True, blank=True)
    youtube_url = models.CharField(max_length=254)
    youtube_id = models.CharField(max_length=254, null=True, blank=True)
    data_caption = models.CharField(max_length=254, null=True, blank=True)
    description = models.CharField(max_length=254, null=True, blank=True)
    active = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return str(self.name)

    def display_performer_names(self):
        return ', '.join([performer.name for performer in self.artists.all()])