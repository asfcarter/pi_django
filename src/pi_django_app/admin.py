from django.contrib import admin

# Register your models here.
from .models import pi_django_app

class pi_django_appAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","time_stamp"]
	
	class Meta:
		model = pi_django_app
	#form = pi_django_appForm

admin.site.register(pi_django_app,pi_django_appAdmin)
