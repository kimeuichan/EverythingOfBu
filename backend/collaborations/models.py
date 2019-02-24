from django.contrib.gis.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    created_time = models.DateTimeField(default=timezone.now)
    
# Create your models here.

class DetailMember(models.Model):
    """Model definition for DetailMember."""

    # TODO: Define fields here
    memberType = models.SmallIntegerField(default=0)
    postId = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for DetailMember."""

        verbose_name = 'DetailMember'
        verbose_name_plural = 'DetailMembers'


