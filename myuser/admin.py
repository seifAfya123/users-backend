from django.contrib import admin
from myuser.models import *
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ( "universty", "governrate")
    list_filter =  ("universty", "governrate" )