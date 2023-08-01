from django.db import models
# AbstractUser to only modify User,  base_user.AbstractUser totally new User
from django.contrib.auth.models import AbstractUser                   
from django.contrib.auth.base_user import BaseUserManager          # import it from base_user

class UserManager(BaseUserManager):
    # normal user 
    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            **other_fields                    #  normal user don't have permissions
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # this method change the fuctionality to create super user
    def create_superuser(self, email, password=None, **other_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        # set the permissions which  are required to be a superuser
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('is_superuser',True)

        if other_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if other_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        
        return self.create_user(email,password=password,**other_fields)
    
# user AbstractUser if wants already exists fields Of django default User otherwise use AbstractBaseUser
# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)

    objects = UserManager()

    # use email fields to login
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []        # there's no required fields
     
    def __str__(self):
        return self.email