from django.contrib import admin
from .models import TypePerson, Person, Movie


class PersonAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'slug', 'aliases', 'typepersona', 'created_at', 'updated']
    prepopulated_fields = {'slug': ('firstname',)}


admin.site.register(Person, PersonAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'genre', 'Release_Year', 'language', 'state', 'created_at', 'updated']
    list_filter = ['state', 'created_at', 'updated']
    list_editable = ['Release_Year', 'state']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Movie, MovieAdmin)
admin.site.register([TypePerson])
