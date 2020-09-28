from django.shortcuts import render, HttpResponse
from datetime import datetime
from website.models import Contact
from django.contrib import messages

# Create your views here.

#Manually
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is home page")

#This is for about page
def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")

#This is for contact page
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        contact = Contact(name=name, email=email, phone=phone, description=description, date= datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

    
    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")

#This is for services page
def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")

def basicPy(request):
    return render(request, 'basicpy.html')

def mllearn(request):
    return render(request, 'mllearn.html')

def robot(request):
    return render(request, 'robot.html')



# Time : 1.50 

