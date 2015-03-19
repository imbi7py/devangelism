from django.contrib.auth.models import User
from django.db.models.signals import post_save
from api.models import Speaker


def create_profile(sender, **kw):
    user = kw["instance"]
    if kw["created"]:
        speaker = Speaker(user=user, username=user.username)
        speaker.save()

post_save.connect(create_profile, sender=User)
