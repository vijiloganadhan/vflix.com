from django.db import models

# Create your models here.
class Category(models.Model):
    cid=models.PositiveIntegerField(unique=True)
    cname=models.CharField(max_length=100)
    poster=models.ImageField(upload_to="poster/")
    def __str__(self):
        return self.cname
class Videos(models.Model):
    vid=models.PositiveIntegerField(unique=True)
    title=models.CharField(max_length=100)
    video=models.FileField(upload_to="videos/")
    category=models.ForeignKey(Category,on_delete=models.CASCADE , related_name="videos")
    def __str__(self):
        return f"{self.title}-{self.category.cname}"
class Seasons(models.Model):
    sid = models.PositiveIntegerField(unique=True)
    snum = models.PositiveBigIntegerField(unique=True)
    simage = models.ImageField(upload_to="season_image/")
    videos = models.ForeignKey(Videos, on_delete=models.CASCADE, related_name="seasons")

    def __str__(self):
        return f"{self.snum}-{self.videos.title}"

    class Meta:
        unique_together = ('snum', 'videos')


class Episodes(models.Model):
    eid = models.PositiveIntegerField(unique=True)
    enum = models.PositiveIntegerField(unique=True)
    videos = models.FileField(upload_to="episode_video/")
    edesc = models.TextField()
    seasons = models.ForeignKey(Seasons, on_delete=models.CASCADE, related_name="episodes")

    def __str__(self):
        return f"{self.enum}-{self.seasons.snum}"

    class Meta:
        unique_together = ('enum', 'seasons')
