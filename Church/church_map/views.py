from django.shortcuts import render

# Create your views here.

def church_map(request):

    return render(request,"church_map/map.html")
