from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import ListView
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.

def jupiter(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            return render(request, 'jupiter.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'jupiter.html', {'all_items': all_items})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    return redirect('jupiter')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('jupiter')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('jupiter')
