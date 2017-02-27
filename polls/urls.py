from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addUser/$', views.add_user_view, name='addUser'),
    url(r'^updateUser/$', views.update_user_view, name='updateUser'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^specie_information/(?P<id_specie>\d+)/$', views.specie_information, name='specieInformation'),
    url(r'^add_comment/(?P<id_specie>\d+)/$', views.add_comment, name='addComment'),
#/(?P<id_specie>\d+)/(?P<text_comment>[\w\-]+)
    url(r'^specie_information_rest/(?P<id_specie>\d+)/$', views.specie_information, name='specieInformationRest'),
]
