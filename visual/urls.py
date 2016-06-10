from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'visual.views.home'),
    url(r'^(?P<id>\d+)', 'visual.views.detail'),
    url(r'^add', 'visual.views.add'),
    url(r'^edit/(?P<id>\d+)/$', 'visual.views.edit'),
    url(r'^type/(?P<id>\d+)', 'visual.views.type_visuals'),
    url(r'^export', 'visual.views.export'),
    url(r'^import', 'visual.views.importVisual'),
    #url(r'^updateallvisual', 'visual.views.updateVisual'),
]