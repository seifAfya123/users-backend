from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myuser.models import User
from django.http import Http404
from myuser.serializers import *
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import AllowAny



class UsersList(APIView):
    def get(self, request):
        user = User.objects.all()
        userserializer = UserSerializer(user, many=True)
        # response_message={"message":"test get response", "usera data":userserializer.data}
        return Response(data= userserializer.data, status=status.HTTP_200_OK)

class UserRegister(generics.CreateAPIView):
    permission_classes =( AllowAny ,)
    serializer_class = RegisterSerializer
    
    ### Func 
    ## Api
        
class OneUser(APIView):
       
    def getobject(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self , request, pk):
        # return query set
        user = self.getobject(pk=pk)
        # convert query to json
        userserializer = UserSerializer(user)
        # return the json response 
        return Response(data=userserializer.data)            
    
    def put(self, request ,pk):
        user = self.getobject(pk=pk)
        userserializer = UserSerializer(user, data = request.data)
        # userserializer = UserSerializer(user)
        if userserializer.is_valid():
            userserializer.save()
            response_message={"message":"updated"}
            return Response(data= response_message, status=status.HTTP_201_CREATED)
        return Response(userserializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    
    def delete(self, request ,pk):
        user = self.getobject(pk=pk)
        user.delete()        
        responseMessage={"message":f"object {pk} deleted succesfuly"}
        return Response(data=responseMessage) 
    