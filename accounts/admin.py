from django.contrib import admin
from .models import  owner

# Register your models here.

# admin.site.register(owner)

class owner_admin(admin.ModelAdmin):
    display= ("user_name", "email", "phone_number")

admin.site.register(owner, owner_admin)