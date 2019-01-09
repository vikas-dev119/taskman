from django.conf.urls import url
from user_manager import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='login'), # Notice the URL has been named
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
]