#Developer : Armando Ruiz Rebollar
from .models import Person, Movie
from .serializers import PersonSerializer, MovieSerializer, MovieFullSerializer, MoviePersonaSerializer, \
    PersonaMovieSerializer, PersonFullSerializer
from rest_framework import generics, viewsets, permissions, status
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate


class PersonAllViewSet(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (AllowAny,)


class MoviePersonAllViewSet(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviePersonaSerializer
    permission_classes = (AllowAny,)


class MovieAllViewSet(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny,)


class PersonMovieAllViewSet(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonaMovieSerializer
    permission_classes = (AllowAny,)


class RegisterUsers(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        token = Token.objects.create(user=user)
        data = {'detail': 'User successfully created ok token' + token.key}

        reply = json.dumps(data)
        return HttpResponse(reply, content_type='application/json')


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(username=username, password=password)
        if user:
            token = Token.objects.get(user_id=user.id)
            data = {"nombre": user.first_name,
                    "apellido": user.last_name,
                    "token": token.key}
        else:
            data = {"error": "Not the Credentials"}
        reply = json.dumps(data)
        return HttpResponse(reply, content_type='application/json')


class MovieFullVieSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieFullSerializer
    permission_classes = (IsAuthenticated,)


class PersonFullVieSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonFullSerializer
    permission_classes = (IsAuthenticated,)


