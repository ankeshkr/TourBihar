from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is aboutpage")

def contactus(request):
    return HttpResponse("this is contactus")

def services(request):
    return HttpResponse("this is servicespage")
