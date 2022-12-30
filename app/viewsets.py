import django_filters
from django_filters import rest_framework as filters
from rest_framework import viewsets

from . import (
    serializers,
    models
)


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = models.Task
        fields = ["id", "title", "category", "completed", "date"]


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TaskFilter
