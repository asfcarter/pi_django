from django.db import models

# Create your models here.
class pi_django_app(models.Model):
	full_name = models.CharField(blank=False,null=True,max_length=100)
	time_stamp = models.DateTimeField(auto_now_add=True,auto_now=False)

	def __unicode__(self):
		return self.full_name
