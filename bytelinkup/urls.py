"""bytelinkup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from blu.views import * 

urlpatterns = [
    path('bytelinkupadmin/', admin.site.urls),
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contactUs/',contactus,name='contactUs'),
    # path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('usereview/',ReviewClient,name='usereview'),

    path('web-design/',web_design_detail_view,name='webdes'),
    path('web-development/',web_development_detail_view,name='webdev'),
    path('ui-ux-design/',ui_ux_design_detail_view,name='uiux'),
    path('digital-marketing/',digital_marketing_detail_view,name='digimar'),
    path('shopify/',shopify_detail_view,name='shopify'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)