from api.models import Speaker, Talk

from rest_framework import viewsets
from api.serializers import (
    SpeakerSerializer, TalkSerializer
)


class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


class TalkViewSet(viewsets.ModelViewSet):
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer
