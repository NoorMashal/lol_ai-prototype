from django.contrib import admin  #Tells the admin interface to add Question as an object that can later be editted.

from . models import Question

admin.site.register(Question)
