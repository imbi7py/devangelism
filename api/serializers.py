from api.models import Talk, Speaker
from rest_framework import serializers


class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Speaker
        fields = ('name', 'title', 'twitter', 'username')


class TalkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Talk
        fields = ('speaker', 'title', )
