from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable1":"Nhi bhai sab ghatia!"
    }
    return render(request,"index.html",context)
def about(request):
    return HttpResponse("This is the aboutpage")
def services(request):
    return HttpResponse("This is the servicespage")
def contact(request):
    return HttpResponse("This is the contactpage")