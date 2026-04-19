from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from .models import PlaylistId, PlaylistVideoId, YoutubeVideoStats, YoutubeVideos



# Create your views here.
def PlaylistId_view(request):
    playlist_id = get_list_or_404(PlaylistId)
    context = {'playlist_id' : playlist_id}
    return render(request, 'PlaylistId.html', context)


def video_list(request):
    video_stats = get_list_or_404(YoutubeVideoStats)
    paginator = Paginator(video_stats, 28)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj' : page_obj}
    return render(request, 'video_list.html', context)


def video_details_view(request, video):
    video_details = get_object_or_404(YoutubeVideoStats, video=video)
    context = {'video_details': video_details}
    return render(request, 'video_details.html', context)