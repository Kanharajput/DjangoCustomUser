from django.contrib import admin
from .models import User
# Register your models here.

# only pass UserAdmin in case there's some change in admin panel
admin.site.register(User)