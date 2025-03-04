from django.db.models import signals
from django.dispatch import receiver

from movies.models import Director
from django.core.cache import cache


@receiver([signals.post_delete,signals.post_save], sender=Director)
def signal_director(sender, instance: Director, **kwargs):
    # Borra la caché cuando se hace un cambio en el modelo Director
    cache.delete("movies_list")