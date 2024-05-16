from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
#from rest_framework.Response import Response
# Create your views here.
from .models import data

def store(request):
 #   return Response('1')

    return HttpResponse({'hello'})
    pass

def ambulance_fetch(request):

    pass

def members(request):
  #template = loader.get_template('myfirst.html')
  return render(request, 'myfirst.html')

def display(request):
    thing = data.objects.last()
    src=thing.source
    print(src)
    dest=thing.destination
    print(dest)
    retu="source--->"+src+"_______destination>"+dest
    print(retu)
    ret={'src':src,'dest':dest}
    print(ret)
    return HttpResponse(thing)

#ok------------------------------------
def store_data(request):
    print('okayyyy')
    if request.method == "POST":
        print('post entered')
        source = request.POST['source']
        destination = request.POST['destination']

        x = data(source=source, destination=destination)  # Correct the model name if necessary
        print('before--------------------------')
        x.save()
        print("-----------------------------")
    return render(request, 'server.html', {})



def ambulance_page(request):
    print("------------------------------------------------callinggggg")
    latest_data = data.objects.last()
    print("------------------------able to fetch ")

    return render(request, 'ambulance.html', {'latest_data': latest_data})

def server_page(request):
    pass