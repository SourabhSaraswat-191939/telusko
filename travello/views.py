from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    # dest1 = Destination()
    # dest1.name = "Mumbai"
    # dest1.desc = "City which never sleeps"
    # dest1.img = 'destination_5.jpg'
    # dest1.price = 705
    # dest1.offer = False
    #
    # dest2 = Destination()
    # dest2.name = "Banglore"
    # dest2.desc = "City which never sleeps"
    # dest2.img = 'destination_6.jpg'
    # dest2.price = 600
    # dest2.offer = True
    #
    # dest3 = Destination()
    # dest3.name = "Ajmer"
    # dest3.desc = "City which never sleeps"
    # dest3.img = 'destination_7.jpg'
    # dest3.price = 350
    # dest3.offer = False
    #
    # dests = [dest1,dest2,dest3]

    s = Destination.objects.all()
    dests = []
    for entry in s:
        if entry.price == 400:
            dests.append(entry)
    return render(request, "index.html",{'dests':dests})