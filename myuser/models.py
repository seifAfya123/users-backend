from django.db import models
from django.contrib.auth.models import User
from myuser.choices import *

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=("User name"), on_delete=models.CASCADE)
    universty = models.CharField(("Universty"), blank=True,null=True , max_length=20, choices= univ_choices)
    governrate = models.CharField(("Governrate"),blank=True,null=True ,max_length=20 , choices= gov_choices)
    
    # def save
    class Meta:
        verbose_name= "Profile"
        
    def __str__(self):
        return self.user.email