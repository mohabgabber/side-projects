from django.db import models

class SpotifyToken(models.Model):
    user = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    refresh_token = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length=50)