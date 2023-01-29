from django.contrib import admin
from .models import Shoe, Storage, Sock

# Register your models here.
admin.site.register(Shoe)
admin.site.register(Storage)
admin.site.register(Sock)