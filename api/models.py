from django.db import models
from django.contrib.auth.models import User


class Speaker(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)  # Populate from phonetool
    twitter = models.CharField(max_length=140)  # twitter

    def __unicode__(self):
        return self.user.username


class Talk(models.Model):
    speaker = models.ForeignKey(Speaker, related_name='talks')
    date = models.DateTimeField()
    duration = models.FloatField(null=True)
    title = models.CharField(max_length=255)  # Talk title
    slides = models.URLField(max_length=600)  # href link
    video = models.URLField(max_length=600)  # href link
    hashtag = models.CharField(max_length=140)  # Twitter hashtag
    notes = models.CharField(max_length=10000)
    ticket_url = models.URLField(max_length=1000)
    campaign_url = models.URLField(max_length=1000)
    approved = models.BooleanField(default=False)
    size = models.IntegerField()
    location = models.CharField(max_length=1000)
    region = models.CharField(max_length=1000)
    event_type = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title + " - " + self.event_type
