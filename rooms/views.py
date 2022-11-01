from django.shortcuts import render
from django.http import Http404
from .models import Room

# Create your views here.


def see_all_room(request):
    rooms = Room.objects.all()
    return render(
        request,
        "all_rooms.html",
        {"rooms": rooms, "title": "Hello! this title comes from django!"})


def see_one_room(request, room_pk):
    try:
        room = Room.objects.get(pk=room_pk)
    except Room.DoesNotExist:
        raise Http404()

    return render(request, "room_detail.html", {"room": room})
