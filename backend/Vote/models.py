from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=30, null=False)
    content = models.TextField(null=False, max_length=100)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    created_time = models.DateField(auto_now_add=True)
    writter = models.ForeignKey(get_user_model(), related_name="topics", on_delete=models.CASCADE)

    def __str__(self):
        """Unicode representation of Topic."""
        return "{} {} - {}".format(self.name, self.start_date, self.end_date)

class Choice(models.Model):
    content = models.CharField(max_length=40)
    topic_id = models.ForeignKey(Topic, related_name="choices", on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.topic_id, self.content)

class Ballot(models.Model):
    voter = models.ForeignKey(get_user_model(), related_name="ballots", on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name="ballots", on_delete=models.CASCADE)
    created_time = models.DateField(auto_now_add=True)


