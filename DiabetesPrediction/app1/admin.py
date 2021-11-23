from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(UserDatas)
admin.site.register(Usernames)