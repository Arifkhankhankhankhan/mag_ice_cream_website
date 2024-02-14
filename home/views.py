from django.shortcuts import render, HttpResponse
from datetime import datetime  # Fix the import statement
from home.models import Contact  # Correct the model import
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        "variable": "you are bloody sweet",  # Corrected the string
    }
    return render(request, 'text.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact= request.POST.get('contact')  # Changed the variable name
        description = request.POST.get('description')  # Changed the variable name

        new_contact = Contact(name=name, email=email, contact=contact, description=description, date=datetime.today())
        new_contact.save()
        messages.success(request, "you profile saved sucessfully")

    return render(request, 'contact.html')



