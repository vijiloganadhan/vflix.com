from django.shortcuts import render
from .models import Category,Videos,Seasons,Episodes
# Create your views here.

def home_views(request):
    cat=Category.objects.all()
    videos=Videos.objects.all()
    context={
        'cat':cat,
        'videos':videos
    }
    return render(request,'home.html',context)
def videos_views(request,ids):
    cat=Category.objects.get(cid=ids)
    v=Videos.objects.filter(category=cat)
    context={
        'videos':v
    }
    return render(request,'videos.html',context)
def seasons_views(request,ids):
    videos=Videos.objects.get(vid=ids)
    seasons=Seasons.objects.filter(videos=videos)
    context={
        'seasons':seasons
    }
    return render(request,'seasons.html',context)
def episodes_views(request,ids):
    season=Seasons.objects.get(sid=ids)
    episodes=Episodes.objects.filter(seasons=season)
    context={
        'episode':episodes
    }
    return render(request,'episodes.html',context)