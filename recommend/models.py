from django.db import models

class Music(models.Model):
    track_name = models.CharField(max_length=255)
    artists_name = models.CharField(max_length=255)
    artist_count = models.IntegerField()
    released_year = models.IntegerField()
    released_month = models.IntegerField()
    released_day = models.IntegerField()
    in_spotify_playlists = models.IntegerField()
    in_spotify_charts = models.IntegerField()
    streams = models.BigIntegerField()
    in_apple_playlists = models.IntegerField()
    in_apple_charts = models.IntegerField()
    in_deezer_playlists = models.IntegerField()
    in_deezer_charts = models.IntegerField()
    in_shazam_charts = models.IntegerField()
    bpm = models.IntegerField()
    key_name = models.CharField(max_length=10)  # Renamed from key_
    mode = models.CharField(max_length=10)  # Renamed from mode_
    danceability = models.FloatField()
    valence = models.FloatField()
    energy = models.FloatField()
    acousticness = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    speechiness = models.FloatField()

    class Meta:
        db_table = 'music_table'  # This tells Django to use the existing table
