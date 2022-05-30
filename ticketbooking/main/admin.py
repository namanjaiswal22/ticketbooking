from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(user_DB)
admin.site.register(events_DB)
admin.site.register(booked_DB)
