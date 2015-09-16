"""pi_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','pi_django_app.views.home', name='home'),
    url(r'Accenture.html$', views.AccenturePage.as_view(), name='Accenture'),
    url(r'ANPR.html$', views.ANPRPage.as_view(), name='ANPR'),
    url(r'apache.html$', views.apachePage.as_view(), name='apache'),
    url(r'Bands_I_like.html$', views.Bands_I_likePage.as_view(), name='Bands_I_like'),
#    url(r'C-optimization.html$', views.C-optimizationPage.as_view(), name='C-optimization'),
    url(r'cricket.html$', views.cricketPage.as_view(), name='cricket'),
    url(r'cv.html$', views.cvPage.as_view(), name='cv'),
    url(r'django.html$', views.djangoPage.as_view(), name='django'),
    url(r'du.html$', views.duPage.as_view(), name='du'),
    url(r'Energy_bus_exercises.html$', views.Energy_bus_exercisesPage.as_view(), name='Energy_bus_exercises'),
    url(r'Energy_bus.html$', views.Energy_busPage.as_view(), name='Energy_bus'),
    url(r'git.html$', views.gitPage.as_view(), name='git'),
    url(r'home.html$', views.homePage.as_view(), name='home'),
    url(r'hosts.html$', views.hostsPage.as_view(), name='hosts'),
    url(r'index.html$', views.IndexPage.as_view(), name='index'),
#    url(r'index.html$', views.Index2Page.as_view(), name='index'),
]
