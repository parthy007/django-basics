from django.shortcuts import render, HttpResponse
from Home.models import Contact

# Create your views here.
def index(request):
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
    return render(request,"contact.html")