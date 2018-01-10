from django.urls import path, re_path
from . import views

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    #/music/album_id
   path('<int:album_id>/', views.detail, name='detail'),
]
