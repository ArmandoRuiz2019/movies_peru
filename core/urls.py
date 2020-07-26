from django.urls import path, include
from . import views
from rest_framework import routers

app_name = "apis_core"

router = routers.DefaultRouter()
router.register('full_movies', views.MovieFullVieSet)
router.register('full_persons', views.PersonFullVieSet)

urlpatterns = [
    path('List_All_Movies/', views.MovieAllViewSet.as_view()),
    path('List_All_Persons/', views.PersonAllViewSet.as_view()),
    path('List_Movies_Persons/', views.MoviePersonAllViewSet.as_view()),
    path('List_Persons_Movies/', views.PersonMovieAllViewSet.as_view()),
    path('Register_New_User/', views.RegisterUsers.as_view()),
    path('Login/', views.LoginView.as_view()),
    path('apis/', include(router.urls)),


]
# http://127.0.0.1:8000/List_Persons_Movies/
# RESTFULL
# http://127.0.0.1:8000/apis/full_movies/
# http://127.0.0.1:8000/apis/full_persons/
# Headers
# Authorization Token da8e23ba89fe62281bff0a12a45195b3ec4454b6
