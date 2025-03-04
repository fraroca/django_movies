from rest_framework import serializers
from .models import Director, Movie, DirectorMovie
from django.contrib.auth.models import User


class MovieSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'year', 'creator')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'movies')

class DirectorSerializer(serializers.ModelSerializer):  # create class to serializer model
    class Meta:
        model = Director
        fields = '__all__'

class DirectorMovieSerializer(serializers.ModelSerializer):  # create class to serializer model
    class Meta:
        model = DirectorMovie
        fields = '__all__'