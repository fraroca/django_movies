from django.db import models



class Director(models.Model):
    nombre = models.CharField(max_length=100)
    anio_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.nombre
class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    directores = models.ManyToManyField(Director, through='DirectorMovie', related_name='movies_director')
    creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title + " - " + self.genre + " - " + str(self.year)

class DirectorMovie(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    porcentaje_participacion = models.DecimalField(max_digits=5, decimal_places=2)  # Porcentaje de participación

    def __str__(self):
        return f'{self.porcentaje_participacion}%'





