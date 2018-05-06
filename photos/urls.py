from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$', views.index, name = 'index'),
    url('^search/', views.search, name = 'search'),
    url('^kenya/', views.kenya, name = 'kenya'),
    url('^nigeria/', views.nigeria, name = 'nigeria'),
]
