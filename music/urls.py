from django.urls import path, re_path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),
    #/music/album_id/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #/music/album_id/favorites/
    # path('<int:album_id>/favorite/', views.favorite, name='favor'),
    
    #/music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
    
    
]
