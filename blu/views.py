from django.shortcuts import render

# Create your views here.

def web_design_detail_view(request):
    return render (request, 'webdesign.html')

def web_development_detail_view(request):
    return render (request, 'web_development.html')

def ui_ux_design_detail_view(request):
    return render (request, 'ui_ux_template.html')

def digital_marketing_detail_view(request):
    return render (request, 'digital_marketing.html')

def shopify_detail_view(request):
    return render (request, 'shopify.html')