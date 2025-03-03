from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'director', views.DirectorViewSet, basename="director")



urlpatterns = [
    path('', views.ListCreateMovieAPIView.as_view(), name='get_post_movies'),
    path('<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),

] + router.urls