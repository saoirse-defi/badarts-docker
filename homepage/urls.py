from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('events', views.events, name='events'),
    path('recording', views.recording, name='recording'),
    path('events/<uuid:event_id>', views.event_page, name='event_page'),
    path('<uuid:artist_id>', views.artist_profile, name='artist_profile'),
    path('gallery', views.gallery, name='gallery'),
]