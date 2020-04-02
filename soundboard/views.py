from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Sound


def index(request):
    sounds = Sound.objects.filter(active=True).order_by('name')

    moods = Sound.objects.values_list(
        'mood', flat=True).distinct().order_by('mood')
    context = {
        'sounds': sounds,
        'moods': moods
    }
    return render(request, 'soundboard/base.html', context)


def dark(request):
    sounds = Sound.objects.filter(active=False).order_by('name')

    moods = Sound.objects.values_list(
        'mood', flat=True).distinct().order_by('mood')
    context = {
        'sounds': sounds,
        'moods': moods
    }
    return render(request, 'soundboard/base.html', context)
