from django.shortcuts import render
from .form import *
from django.contrib import messages

def home(req):
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
        if form.is_valid():
            form.save()
            form = ContactForm()
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