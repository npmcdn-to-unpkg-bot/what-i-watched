from django.conf.urls import url
import visual.views

app_name = 'visual'

urlpatterns = [
    url(r'^$', 'visual.views.home', name='home'),
    url(r'^(?P<id>\d+)', 'visual.views.detail', name='detail'),
    url(r'^add', 'visual.views.add', name='add'),
    url(r'^edit/(?P<id>\d+)/$', 'visual.views.edit', name='edit'),
    url(r'^type/(?P<id>\d+)', 'visual.views.type_visuals'),
    url(r'^ajax_submit_review', 'visual.views.ajax_submit_review'),
    url(r'^export', 'visual.views.export'),
    url(r'^import', 'visual.views.importVisual'),
    #url(r'^updateallvisual', 'visual.views.updateVisual'),
]