from django.contrib import admin
from .models import *

#class H1Admin(admin.ModelAdmin):
    #readonly_fields = ("dni", )



admin.site.register(Hoja1)  #, H1Admin

admin.site.register(Hoja2)

admin.site.register(Capacitacion)
