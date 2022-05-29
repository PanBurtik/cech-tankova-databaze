from django.views.generic import ListView, DetailView
from multiprocessing import context
from django.shortcuts import render
from tank.models import Tank, Characteristics


# Create your views here.


def index(request):
    num_tanks = Tank.objects.all().count

    tanks = Tank.objects.order_by('name')[:3]


    context ={
        'num_tanks': num_tanks,
        'tanks': tanks,

    }

    return render(request, 'index.html', context = context)


class TankListView(ListView):
    model = Tank

    context_object_name = 'tanks'
    template_name = 'list.html'


class TankDetailView(DetailView):
    model = Tank

    context_object_name = 'tanks_detail'
    template_name = 'detail.html'


class CharacteristicsListView(ListView):
    model = Characteristics

    context_object_name = 'characteristics'
    template_name = 'detail.html'


class CharacteristicsDetailView(DetailView):
    model = Characteristics

    context_object_name = 'characteristics_detail'
    template_name = 'detail.html'
