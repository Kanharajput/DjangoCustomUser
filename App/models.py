from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    # normal user 
    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # this method change the fuctionality to create super user
    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    

# Create your models here.
class User(AbstractUser):
    username = models.CharField(default=None, null= True , max_length=10) 
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # don't write is_staff it will added automatically

    objects = UserManager()

    # use email fields to login
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []        # there's no required fields
     
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
