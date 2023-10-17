from django.shortcuts import render
from .form import *
from django.contrib import messages
from contact.models import *
def home(req):
    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid:
            names = req.POST.get('name')
            emails = req.POST.get('email')
            subjects = req.POST.get('subject')
            Category = req.POST.get('Category')
            saveContact = Contact.objects.create(name=names,email=emails,subject=subjects,message=Category)
            messages.success(req, 'Form submitted successfully!')
            # form.save()
            return render(req,'index.html')

    service = Service.objects.all()
    return render(req,'index.html',{'service':service})

def about(req):
    return render(req,'about-us.html')
def services(req):
    service = Service.objects.all()
    return render(req,'our-services.html',{'service':service})

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            names = request.POST.get('name')
            emails = request.POST.get('email')
            subjects = request.POST.get('subject')
            Category = request.POST.get('Category')
            saveContact = Contact.objects.create(name=names,email=emails,subject=subjects,message=Category)
            messages.success(request, 'Form submitted successfully!')
            # return redirect('success')
            return render(request,'contact-us.html',{'form':form})
            # Process the form data
    else:
        form = ContactForm()
    return render(request,'contact-us.html',{'form': form})

def ReviewClient(request):
    print("yes\n")
    if request.method == 'POST':
        form =  Review(request.POST,request.FILES)
        if form.is_valid():
            # print(form.image)
            print("Received form data:", form.cleaned_data)
            s = form.save()
            print(s)
            form = Review()
            messages.success(request, 'Form submitted successfully!')
            # return redirect('success')
            return render(request,'Review.html',{'form':form})
            # Process the form data
    else:
        form = Review()
    return render(request,'Review.html',{'form': form})
# def contact(request):
#     # print(request.name)
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save(commit=False)
#             # Process the form data
#     else:
#         form = ContactForm()
#     return render(request, 'contact-us.html', {'form': form})