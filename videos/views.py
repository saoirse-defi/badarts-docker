import uuid
from django.shortcuts import render
from .models import Video


def videos(request):
    videos = Video.objects.all()

    template = 'videos/videos.html'
    context = {
        'videos': videos,
    }
    return render(request, template, context)