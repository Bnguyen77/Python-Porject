from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^/register$', views.register),
    url(r'^/dashboard$', views.dashboard),   # This line has changed! Notice that urlpatterns is a list, the comma is in
    #Please check the regex for category
    url(r'^/products/(?P<category>\w+)$', views.productCategory),
    url(r'^/products/(?P<id>\d+)$', views.productPage),



]   