from rest_framework import serializers
from .models import Person, Movie


class PersonFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['lastname', 'firstname', 'aliases', 'typepersona']


class PersonSerializer(serializers.ModelSerializer):
    # Esto te trae el nombre no el ID
    type_name = serializers.CharField(source='typepersona.type')

    class Meta:
        model = Person
        fields = ['lastname', 'firstname', 'aliases', 'type_name', 'photo']


class MovieFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'sipnosis', 'Release_Year', 'language', 'genre', 'Actor_Actress', 'Director', 'Producer']
        # fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'sipnosis', 'Release_Year', 'get_num_roman', 'language', 'genre', 'top']


class MoviePersonaSerializer(serializers.ModelSerializer):
    Actor_Actress = PersonSerializer(many=True, read_only=True)
    Director = PersonSerializer(many=True, read_only=True)
    Producer = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['title', 'sipnosis', 'Release_Year', 'get_num_roman', 'language', 'genre', 'top', 'Actor_Actress',
                  'Director',
                  'Producer']


class PersonaMovieSerializer(serializers.ModelSerializer):
    actor_actress = MovieSerializer(many=True, read_only=True)
    director = MovieSerializer(many=True, read_only=True)
    producer = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ['lastname', 'firstname', 'aliases', 'photo', 'actor_actress', 'director', 'producer']


