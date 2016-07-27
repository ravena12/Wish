from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'my_travel_index'),
    url(r'^edit/(?P<id>\d+)$', views.pedit, name = 'my_travel_pedit'),
    url(r'^register/$', views.register, name = 'my_wish_register'),
    url(r'^login/$', views.processlogin, name = 'my_wish_login'),
    url(r'^logout/$', views.logout, name = 'my_wish_logout'),
    url(r'^process/$', views.processregister, name = 'my_register_process'),
    url(r'^home/$', views.home, name = 'my_wish_home'),
    url(r'^profile/(?P<id>\d+)$', views.userProfile, name = 'my_wish_profile'),
    url(r'^create/$', views.processwish, name = 'my_wish_add'),
    url(r'^createproduct/$', views.createproduct, name = 'my_wish_addpage'),
    url(r'^product/(?P<id>\d+)$', views.product, name = 'my_wish_product'),
    url(r'^join/(?P<id>\d+)$', views.join, name = 'my_wish_join'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name = 'my_wish_destroy'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name = 'my_wish_delete'),
]

