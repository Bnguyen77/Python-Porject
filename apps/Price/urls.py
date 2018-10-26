from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^register1$', views.register1),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    # #Please check the regex for category
    url(r'^products/(?P<category>\w+)$', views.productCategory),
    url(r'^product/(?P<id>\d+)$', views.productPage),
    # url(r'^product/(?P<id>\d+)$', views.productPage),
]   