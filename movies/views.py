from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Director, Movie
from .permissions import IsOwnerOrReadOnly
from .serializers import DirectorSerializer, MovieSerializer
from .pagination import CustomPagination
from .filters import MovieFilter
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status


class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class DirectorFilterSet(filters.FilterSet):

    class Meta:
        model = Director
        fields = {
            'nombre': ['exact', 'icontains', 'in', 'startswith', 'endswith', 'istartswith', 'iendswith'],
            'id': ['exact', 'gt', 'lt', 'gte', 'lte'],
        }


class DirectorViewSet(viewsets.ModelViewSet):
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, filters.DjangoFilterBackend, OrderingFilter]
    filterset_class = DirectorFilterSet
    ordering_fields = ['id','nombre']

    def get_queryset(self):
        # Aquí simplemente devuelves el queryset, no cachees los resultados aquí
        return Director.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    '''def list(self, request, *args, **kwargs):
        cache_key = "movies_list"

        # Intentar obtener la respuesta desde la caché
        cached_data = cache.get(cache_key)

        if cached_data:
            # Si los datos están en caché, devolverlos
            return Response(cached_data, status=status.HTTP_200_OK)
        else:
            # Si no están en caché, obtener el queryset
            directors = self.get_queryset()

            # Serializar los datos
            serialized_data = DirectorSerializer(directors, many=True).data

            # Almacenar los datos serializados en la caché por 10,000 segundos
            cache.set(cache_key, serialized_data, timeout=10000)

            # Devolver los datos serializados
            return Response(serialized_data, status=status.HTTP_200_OK)'''



