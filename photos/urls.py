from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$', views.index, name = 'index'),
    url('^search/', views.search, name = 'search'),
]
