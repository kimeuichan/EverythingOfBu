from django.contrib.gis.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    writter = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    isAlive = models.BooleanField(default=True)
    
# Create your models here.


class NeedMember(models.Model):
    """Model definition for DetailMember."""

    # TODO: Define fields here
    memberType = models.SmallIntegerField(default=0)
    post = models.ForeignKey('Post', related_name='members', on_delete=models.CASCADE, null=True, blank=True)
    isRecruit = models.BooleanField(default=True)

    # def __str__(self):
    #     return '%d : %s : %s' % (123, self.memberType, self.isRecruit)


