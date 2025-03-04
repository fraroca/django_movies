from django.contrib import admin
from .models import Director, Movie, DirectorMovie

class DirectorMovieInline(admin.TabularInline):
    model = DirectorMovie
    extra = 1
    fields = ('director', 'porcentaje_participacion')
    autocomplete_fields = ['director']  # Permite autocompletar el nombre del director

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'year')
    inlines = [DirectorMovieInline]

class DirectorAdmin(admin.ModelAdmin):
    search_fields = ['nombre']  # Define search_fields para autocomplete_fields

admin.site.register(Movie, MovieAdmin)
admin.site.register(Director, DirectorAdmin)  # Registra Director con DirectorAdmin
admin.site.register(DirectorMovie)
