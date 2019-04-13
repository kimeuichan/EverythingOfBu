from django.db import models
from django.contrib.auth import get_user_model

# class Category(models.Model):
#     type = models.IntegerField(null=False)
#     name = models.CharField

class Topic(models.Model):
    title = models.CharField(max_length=30, null=False)
    content = models.TextField(null=False, max_length=100)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    created_time = models.DateField(auto_now_add=True)
    writter = models.ForeignKey(get_user_model(), related_name="topics", on_delete=models.CASCADE)

    def __str__(self):
        """Unicode representation of Topic."""
        return "{} {} - {}".format(self.title, self.start_date, self.end_date)

class Choice(models.Model):
    topic_id = models.ForeignKey(Topic, related_name="choices", on_delete=models.CASCADE)
    content = models.CharField(max_length=40)

    def __str__(self):
        return "{} - {}".format(self.topic_id, self.content)

class Ballot(models.Model):
    voter = models.ForeignKey(get_user_model(), related_name="ballots", on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name="ballots", on_delete=models.CASCADE)
    created_time = models.DateField(auto_now_add=True)


