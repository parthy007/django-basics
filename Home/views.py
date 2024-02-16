from django.shortcuts import render, HttpResponse, redirect
from Home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"services.html")
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        contact = Contact(name=name, email=email, address=address, city=city, zip=zip)
        contact.save()
        messages.success(request, "Your form is saved!!")
    return render(request,"contact.html")

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:   
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')