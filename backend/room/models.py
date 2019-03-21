# from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

def room_photo_path(instance, filename):
    return 'images/room_{}/{}'.format(instance.id, filename)

class Room(models.Model):
    """Model definition for Room."""
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    location = models.PointField()
    photo = models.FileField(null=True, upload_to=room_photo_path)
    writter = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='rooms')
    created_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.id is None:
            temp_photo = self.photo
            self.photo = None
            super().save(*args, **kwargs)
            self.photo = temp_photo
        super().save(*args, **kwargs)

class RoomScore(models.Model):
    score = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
    )
    price = models.IntegerField()
    is_lived = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    population = models.SmallIntegerField(default=1)
    deposit = models.IntegerField(null=True, blank=True)
    room_no = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='scores')
    reviewer = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='roomReviews')
    created_time = models.DateTimeField(auto_now_add=True)