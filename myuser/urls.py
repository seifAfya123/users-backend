from django.urls import path , include
from myuser.views import *
urlpatterns = [
    
    path("testuser/",UsersList.as_view(), name = "testuser"),
    path("testuser/<int:pk>",OneUser.as_view(), name = "testoneuser"),
    path("createuser/", UserRegister.as_view() , name = "regiserUser"),
]

