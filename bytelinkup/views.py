from django.shortcuts import render
from .form import *

def home(req):
    service = Service.objects.all()
    return render(req,'index.html',{'service':service})

def about(req):
    return render(req,'about-us.html')
def services(req):
    return render(req,'our-services.html')

def contactus(request):
    print(request)
    print("errrdf")
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Process the form data
    else:
        form = ContactForm()
    return render(request,'contact-us.html',{'form': form})

def contact(request):
    # print(request.name)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            # Process the form data
    else:
        form = ContactForm()
    return render(request, 'contact-us.html', {'form': form})