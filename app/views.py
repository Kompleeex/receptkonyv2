from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import *
from .forms import *
from .filters import *


def index(request):
    receptek = Recept.objects.all()
    filter = ReceptFilter(request.GET, queryset = receptek)

    context = {
        'receptek': receptek,
        'filter':filter
    }

    return render(request, 'receptek.html', context = context)


def receptUpload(request):
    form = ReceptForm(request.POST or None)
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect(index)
    else:
        form = ReceptForm()

    context = {
        'form': form
    }
    return render(request, 'upload.html', context = context)


def receptDelete(request, id):
    recept = get_object_or_404(Recept, pk = id)
    recept.delete()

    return redirect(index)