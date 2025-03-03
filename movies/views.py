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
        return Director.objects.all()




