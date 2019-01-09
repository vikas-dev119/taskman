from django.conf.urls import url
from . import views
from packages.decorators import is_user
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', is_user(views.Index.as_view()), name='activity-list'),
]