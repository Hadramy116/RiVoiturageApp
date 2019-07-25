from django.contrib import admin

# Register your models here.
from .models import Traget, Client, Chauffeur, Voiture

admin.site.register(Traget)
admin.site.register(Client)
admin.site.register(Chauffeur)
admin.site.register(Voiture)