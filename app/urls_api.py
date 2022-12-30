from rest_framework.routers import DefaultRouter

from app import (
    viewsets
)

api_urlpatterns = []

task_router = DefaultRouter()

task_router.register(
    r'^api/task',
    viewsets.TaskViewSet,
    basename="task"
)

api_urlpatterns += task_router.urls
