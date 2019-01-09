from django.conf.urls import url
from . import views
from packages.decorators import is_user
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', is_user(views.Index.as_view()), name='task-list'), # Notice the URL has been named
    url(r'^add/$', is_user(views.AddTask.as_view()), name='task-add'),
    url(r'^task-delete/(?P<task_id>[0-9]+)$', is_user(views.DeleteTask.as_view()), name='task-delete'),
    url(r'^ChangeStatus/$', csrf_exempt(views.ChangeStatus.as_view()), name='change-task-status'),
]