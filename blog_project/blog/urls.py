from django.contrib import admin
from django.urls import path,re_path
from blog import views

urlpatterns = [
    path('', views.home_view),
    #path('post_view/(', views.get_post),
    re_path(r'^view_post/(?P<id>\d+)', views.get_post),
    path('write_post', views.write_post),

]
