from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Artist, Release, Event, Photo


def index(request):
    artists = Artist.objects.all()
    releases = Release.objects.all()
    events = Event.objects.all()
    photos = Photo.objects.all()

    template = 'homepage/index.html'
    context = {
        'artists': artists,
        'releases': releases,
        'events': events,
        'photos': photos
    }

    return render(request, template, context)


def contact(request):

    template = 'homepage/contact.html'
    context = {}

    return render(request, template, context)


def events(request):
    event_list = Event.objects.all()

    template = 'homepage/events.html'
    context = {
        'event_list': event_list,
    }

    return render(request, template, context)


def event_page(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    template = 'homepage/event_page.html'
    context = {
        'event': event,
    }

    return render(request, template, context)


def artist_profile(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    releases = Release.objects.all()

    template = 'homepage/artist_profile.html'
    context = {
        'artist': artist,
        'releases': releases,
    }

    return render(request, template, context)


def recording(request):

    template = 'homepage/recording.html'
    context = {}

    return render(request, template, context)


def gallery(request):

    photos = Photo.objects.all()

    template = 'homepage/gallery.html'
    context = {
        'photos': photos,
    }

    return render(request, template, context)