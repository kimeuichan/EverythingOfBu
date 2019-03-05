from django.contrib.gis.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    writter = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    
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


