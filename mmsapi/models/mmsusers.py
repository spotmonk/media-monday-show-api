from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

class MMSUser(models.Model):
    bio = models.CharField(max_length=200)
    profile_image_url = models.CharField(max_length=200)
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    user_type = models.IntegerField()
