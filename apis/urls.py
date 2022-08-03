from django.urls import include, path
from rest_framework import routers
from . import views

#from .views import ArtistAPIViewset

#router = routers.DefaultRouter()

#router.register(r'artists/', api_artist_view, basename='Artist')

urlpatterns = [
    path('<uuid:artist_id>/', views.api_artist_view, name='artistAPI'),
    path('api-auth/', include('rest_framework.urls')),
]