from django.shortcuts import render

def static_handler(request):
    return render(request, "static_handler.html")
# Create your views here.
