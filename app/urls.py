from django.urls import path, include

from app import conf
from app.urls_api import api_urlpatterns

urlpatterns = []

urlpatterns += [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls'))
]

from app.views import task

urlpatterns += [
    # task
    path(
        '',
        task.List.as_view(),
        name=conf.TASK_LIST_URL_NAME
    ),
    path(
        'task/full/',
        task.ListFull.as_view(),
        name='TASK_list_full'
    ),
    path(
        'task/create/',
        task.Create.as_view(),
        name=conf.TASK_CREATE_URL_NAME
    ),
    path(
        'task/<int:pk>/',
        task.Detail.as_view(),
        name=conf.TASK_DETAIL_URL_NAME
    ),
    path(
        'task/<int:pk>/update/',
        task.Update.as_view(),
        name=conf.TASK_UPDATE_URL_NAME
    ),
    path(
        'task/<int:pk>/delete/',
        task.Delete.as_view(),
        name=conf.TASK_DELETE_URL_NAME
    ),
    path(
        'task/list/json/',
        task.TaskListJson.as_view(),
        name=conf.TASK_LIST_JSON_URL_NAME
    )
]

urlpatterns += api_urlpatterns