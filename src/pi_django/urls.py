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
    url(r'C_optimization.html$', views.C_optimizationPage.as_view(), name='C_optimization'),
    url(r'cricket.html$', views.cricketPage.as_view(), name='cricket'),
    url(r'cv.html$', views.cvPage.as_view(), name='cv'),
    url(r'django.html$', views.djangoPage.as_view(), name='django'),
    url(r'du.html$', views.duPage.as_view(), name='du'),
    url(r'Energy_bus_exercises_Feb_2017.html$', views.Energy_bus_exercisesFeb2017Page.as_view(), name='Energy_bus_exercisesFeb2017'),
    url(r'Energy_bus_exercises_Dec_2016.html$', views.Energy_bus_exercisesDec2016Page.as_view(), name='Energy_bus_exercisesDec2016'),
    url(r'Energy_bus_exercises_Nov_2016.html$', views.Energy_bus_exercisesNov2016Page.as_view(), name='Energy_bus_exercisesNov2016'),
    url(r'Energy_bus_exercises_July_2016.html$', views.Energy_bus_exercisesJuly2016Page.as_view(), name='Energy_bus_exercisesJuly2016'),
    url(r'Energy_bus_exercises_June_2016.html$', views.Energy_bus_exercisesJune2016Page.as_view(), name='Energy_bus_exercisesJune2016'),
    url(r'Energy_bus_exercises_May_2016.html$', views.Energy_bus_exercisesMay2016Page.as_view(), name='Energy_bus_exercisesMay2016'),
    url(r'Energy_bus_exercises_Apr_2016.html$', views.Energy_bus_exercisesApr2016Page.as_view(), name='Energy_bus_exercisesApr2016'),
    url(r'Energy_bus_exercises_Mar_2016.html$', views.Energy_bus_exercisesMar2016Page.as_view(), name='Energy_bus_exercisesMar2016'),
    url(r'Energy_bus_exercises_Oct_2014.html$', views.Energy_bus_exercisesOct2014Page.as_view(), name='Energy_bus_exercisesOct2014'),
    url(r'Energy_bus.html$', views.Energy_busPage.as_view(), name='Energy_bus'),
    url(r'git.html$', views.gitPage.as_view(), name='git'),
    url(r'hosts.html$', views.hostsPage.as_view(), name='hosts'),
    url(r'index.html$', views.IndexPage.as_view(), name='index'),
    url(r'java.html$', views.javaPage.as_view(), name='java'),
    url(r'Lou_Andy_things_to_do.html$', views.Lou_Andy_things_to_doPage.as_view(), name='Lou_Andy_things_to_do'),
    url(r'Lou_Andy_things_to_do_2017.html$', views.Lou_Andy_things_to_do2017Page.as_view(), name='Lou_Andy_things_to_do_2017'),
    url(r'ls_ll.html$', views.ls_llPage.as_view(), name='ls_ll'),
    url(r'LTE.html$', views.LTEPage.as_view(), name='LTE'),
    url(r'map.html$', views.mapPage.as_view(), name='map'),
    url(r'mediawiki_tikiwiki.html$', views.mediawiki_tikiwikiPage.as_view(), name='mediawiki_tikiwiki'),
    url(r'Modulation.html$', views.ModulationPage.as_view(), name='Modulation'),
    url(r'Mortgage.html$', views.MortgagePage.as_view(), name='Mortgage'),
    url(r'nsn.html$', views.nsnPage.as_view(), name='nsn'),
    url(r'raspberry_pi.html$', views.raspberry_piPage.as_view(), name='raspberry_pi'),
    url(r'Real_timeOS.html$', views.Real_timeOSPage.as_view(), name='Real_timeOS'),
    url(r'Renesas.html$', views.RenesasPage.as_view(), name='Renesas'),
    url(r'speech_codec.html$', views.speech_codecPage.as_view(), name='speech_codec'),
    url(r'symbolic_links.html$', views.symbolic_linksPage.as_view(), name='symbolic_links'),
    url(r'The_Secret.html$', views.The_SecretPage.as_view(), name='The_Secret'),
    url(r'Things_to_do.html$', views.Things_to_doPage.as_view(), name='Things_to_do'),
    url(r'home.html$', views.homePage.as_view(), name='home'),
    url(r'Personal.html$', views.PersonalPage.as_view(), name='Personal'),
    url(r'SOLID_principles.html$', views.SOLID_principlesPage.as_view(), name='Personal'),
    url(r'Excel_tips.html$', views.ExceltipsPage.as_view(), name='Personal'),
    url(r'House_plan.html$', views.HousePlanPage.as_view(), name='Personal'),
    url(r'Virtual_machine.html$', views.VirtualMachinePage.as_view(), name='Personal'),
#    url(r'index.html$', views.Index2Page.as_view(), name='index'),
]
