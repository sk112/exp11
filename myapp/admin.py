from django.contrib import admin
from .models import *

admin.site.register(Person)
admin.site.register(Album)
admin.site.register(Musician)