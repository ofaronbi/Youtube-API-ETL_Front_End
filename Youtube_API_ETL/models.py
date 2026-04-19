from django.db import models

# Create your models here.
class PlaylistId(models.Model):
    channel_id = models.CharField(unique=True, max_length=100)
    uploads_id = models.CharField(max_length=100)
    call_date = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'playlist_id'


class PlaylistVideoId(models.Model):
    video_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'playlist_video_id'


class YoutubeVideoStats(models.Model):
    video = models.ForeignKey('YoutubeVideos', models.DO_NOTHING)
    snapshot_date = models.DateField()
    view_count = models.BigIntegerField(blank=True, null=True)
    like_count = models.BigIntegerField(blank=True, null=True)
    comment_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'youtube_video_stats'
        unique_together = (('video_id', 'snapshot_date'),)


class YoutubeVideos(models.Model):
    video_id = models.CharField(primary_key=True, max_length=50)
    channel_title = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=20, blank=True, null=True)
    image_url = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'youtube_videos'