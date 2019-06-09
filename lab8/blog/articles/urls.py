from django.urls import path, re_path
from articles import views

urlpatterns = [
    path('articles/', views.archive, name='archive'),
    re_path(r'^article/(?P<article_id>\d+)/$', views.get_article,  name='get_article'), 
    re_path(r'^article/new/',  views.create_post, name='create_post'), 
    re_path(r'^login/',  views.registration, name='registration'),
    re_path(r'^enter/',  views.avtorisation, name='avtorisation'), 
]
