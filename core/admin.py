from django.contrib import admin
from .models import Owner, Cat, Landlord, Property, Application

admin.site.register(Owner)
admin.site.register(Cat)
admin.site.register(Landlord)
admin.site.register(Property)
admin.site.register(Application)