from myuser.models import *
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
# from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    #is_active = serializers.BooleanField()
    #is_user_full_active = serializers.BooleanField()
    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
            'email', 'first_name', 'last_name')
        
    #def get_query_set(self,)
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        #elif attrs['password'] != attrs['password2']:
            # Create CustomeLogic
        return attrs
        ### Create Custom Super User # NoT Full Active
    def create(self, validated_data):
        
            user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_active = True,
            is_staff = True,
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
    #         user = User.objects.create(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'],
    #         last_name=validated_data['is_active'],
    #         )
    #         if user.is_active != True:
    #             #user = 
    #             is_active = False
    #             is_staff = False
    #         else:
    #             is_active = True
    #             is_staff = True
                
    #         user.set_password(validated_data['password'])
    #         user.save()
    #         return user
    #    ### Create Custom Super User # Full Active
    #         user = User.objects.create(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'],
    #         is_active = False,
    #         is_staff = False,
    #         )
    #         user.set_password(validated_data['password'])
    #         user.save()
    #         last_object = User.objects.last()
    #         profile = Profile.objects.create(
    #             user=last_object
    #         )
    #         profile.save()
    #         return user