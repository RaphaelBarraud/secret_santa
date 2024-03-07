from django.contrib import admin

from .models import Participant, Blacklist

admin.site.register(Participant)
admin.site.register(Blacklist)