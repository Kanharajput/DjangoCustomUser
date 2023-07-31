from django.contrib.auth.models import BaseUserManager
from .models import User

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError("Users must have an email address")

        user.set_password(password)
        user = self.model(
            email=self.normalize_email(email)
        )
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user.is_admin = True
        user = self.create_user(
            email,
            password=password,  
        )
        user.save(using=self._db)
        return user