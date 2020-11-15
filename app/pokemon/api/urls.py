from django.urls import path, include
# from rest_framework_simplejwt import views as jwt_views
from django.conf.urls import url
from .views import PokemonDetails


urlpatterns = [
    # Forms
    path('pokemon/<str:name>/', PokemonDetails.as_view(), name='pokemon_details'),
]
