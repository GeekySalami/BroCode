from django.shortcuts import render

def Home (request):
    return render(request,"navigation/base_navigation.html")
# Create your views here.
