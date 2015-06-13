from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home),
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^python/$', views.python, name='python'),
    url(r'^javascript/$', views.javascript, name='javascript'),
    url(r'^learning_stuffs/$', views.learning_stuffs, name='learning_stuffs'),
    url(r'^balls/$', views.balls, name='balls'),
    url(r'^horse/$', views.horse, name='horse'),
    url(r'^finefinder/$', views.finefinder, name='finefinder'),
    url(r'^learning_stuffs/$', views.learning_stuffs, name='learning_stuffs'),
]