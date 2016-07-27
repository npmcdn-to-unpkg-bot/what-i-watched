from django.conf.urls import url
import userprofile.views

app_name = 'userprofile'

urlpatterns = [
    url(r'^(?P<id>\d+)', 'userprofile.views.detail', name='detail'),
    url(r'^edit/(?P<id>\d+)/$', 'userprofile.views.edit', name='edit'),
]