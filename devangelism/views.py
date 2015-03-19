from django.shortcuts import render, get_object_or_404
from django.db.models import Count

from api.models import Speaker, Talk


def home(request):
    talks = Talk.objects.all().order_by('date')[:5]
    resp = {'talks': talks}
    return render(request, 'index.html', resp)


def speaker(request, username):
    speaker = get_object_or_404(
        Speaker, user__username=username)

    resp = {'speaker': speaker}
    return render(request, 'speaker.html', resp)


def reporting(request):
    speakers = Speaker.objects.all().annotate(num_talks=Count('talks'))
    resp = {'speakers': speakers}
    return resp
