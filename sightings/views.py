from django.shortcuts import render
from sightings.models import Squirrel
from django.shortcuts import get_object_or_404
from .forms import SquirrelForm, SquirrelFullForm
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models import Avg, Max, Min, Count


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

def stats(request):
    count = Squirrel.object.count()
    ratio = Squirrel.objects.filter(Shift = 'AM' ).count()/Squirrel.objects.filter(Shift = 'PM' ).count()
    avg_lat  = Squirrel.objects.aggregate(Avg('Latitude'))
    avg_long = Squirrel.objects.aggregate(Avg('Longitude'))
    adult_no = Squirrel.objects.filter(Age = 'Adult' ).count()
    run_perct = Squirrel.objects.filter(Running = True ).count()/count


    context = {
            'Count_Squirrels': count,
            'Avg_Lattitude': avg_lat,
            'Avg_Longitude': avg_long
            'AM/PM ratio': ratio
            'Adult_Squirrel_Count': adult_no
            'Running_perct': run_perct
            }

    return render(request, 'sightings/stats.html', context)



# Create your views here.
