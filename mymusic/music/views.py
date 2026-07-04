from django.shortcuts import render
from .models import Track

def music_list(request):
    all_tracks = Track.objects.all()
    context = {
        'tracks': all_tracks
    }
    return render(request, 'music/track_list.html', context)