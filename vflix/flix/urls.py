from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.home_views,name="home"),
    path("videos/<int:ids>",views.videos_views,name="videos"),
    path("seasons/<int:ids>",views.seasons_views,name="seasons"),
    path('episodes/<int:ids>',views.episodes_views,name="episodes"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)