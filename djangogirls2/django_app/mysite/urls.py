from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list, name ='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name ='post_detail'),
    url(r'^post/(?P<pk>\d+)/modify/$', views.post_modify, name='post_modify'),
    url(r'^post/create/$', views.post_create, name = 'post_create'),

    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete')
]
