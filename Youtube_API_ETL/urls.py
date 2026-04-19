from django.urls import path
from . import views as v


app_name = 'youtubeApi'

urlpatterns = [
    path('playlist_id/', v.PlaylistId_view, name='listId'),
    path('video_list/', v.video_list, name='video_list'),
    path('<str:video>/', v.video_details_view, name='video_details'),
]