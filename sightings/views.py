from django.shortcuts import render
from sightings.models import Squirrel
from django.shortcuts import get_object_or_404
from .forms import SquirrelForm, SquirrelFullForm
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import redirect

def lists(request):
    sightings = Squirrel.objects.all()
    context = {
            'squirrels': sightings,
            }
    return render(request,'sightings/lists.html',context)


def update(request,squirrel_id):
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=squirrel_id)
    if request.method=='POST':
        form = SquirrelForm(request.POST,instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
        else:
            return JsonResponse({'error':form.errors},status=400)

    form = SquirrelForm(instance=squirrel)
    context ={
            'form':form
            }
    return render(request, 'sightings/update.html', context)

def create(request):

    if request.method=='POST':
        fullform = SquirrelFullForm(request.POST)
        if fullform.is_valid():
            fullform.save()
            return redirect('/sightings/')
        else:
            return JsonResponse({'error':fullform.errors},status=400)
    fullform = SquirrelFullForm()

    context ={
            'fullform':fullform
            }
    return render(request, 'sightings/create.html', context)

# Create your views here.
