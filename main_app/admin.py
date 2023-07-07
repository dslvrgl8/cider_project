from django.contrib import admin
from .models import Cider, Flavor, Favorite # import the Artist model from models.py
# Register your models here.

admin.site.register(Cider) # this line will add the model to the admin panel

admin.site.register(Flavor)

admin.site.register(Favorite)