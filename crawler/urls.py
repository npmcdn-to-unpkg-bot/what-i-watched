from django.conf.urls import url
import crawler.views

app_name = 'crawler'

urlpatterns = [
    url(r'^zhihu_get_pic', 'crawler.views.zhihu_get_pic'),
]