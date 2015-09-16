from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.db import models

# Create your models here.
class CustomUserManager(BaseUserManager):
	def create_user(self, first_name, is_admin, password = None):
		user = self.model(first_name = first_name, is_admin = is_admin)
		return user

        def create_superuser(self, first_name, is_admin, password):
                user = self.model(first_name = first_name, is_admin = is_admin)
		user.is_admin = True
		#user.is_staff = True
		#user.is_superuser = True
		user.set_password(password)
		user.save()
                return user
	


class CustomUser(AbstractBaseUser):
#	username = models.CharField(max_length=254, unique=True)
	first_name = models.CharField(max_length=254, unique=True)
	is_admin = models.BooleanField()

	USERNAME_FIELD = 'first_name'
	REQUIRED_FIELDS = ['is_admin']

        @property
        def is_staff(self):
                return self.is_admin

        @property
        def is_superuser(self):
                return self.is_admin

	def has_perm(self, perm, obj=None):
		return self.is_admin

        def has_module_perms(self, app_label):
                return self.is_admin

	def get_short_name(self):
		return self.first_name

        def get_full_name(self):
                return self.first_name

	objects = CustomUserManager()
