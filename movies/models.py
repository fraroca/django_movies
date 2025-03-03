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
    director = models.ForeignKey(Director, related_name='movie_director', on_delete=models.CASCADE,blank=True,null=True)
    creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title + " - " + self.genre



