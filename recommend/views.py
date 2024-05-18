from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Music


def home(request):
    music_list = Music.objects.all()
    return render(request, 'music_table.html', {'music_list': music_list})
    # return HttpResponse("Here is the recommender!!")
