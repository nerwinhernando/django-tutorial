from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from serializerrelations import views

urlpatterns = format_suffix_patterns([
    url(r'^albums/$', views.album_list),
    url(r'^albums/(?P<pk>[0-9]+)/$', views.album_detail),
])
