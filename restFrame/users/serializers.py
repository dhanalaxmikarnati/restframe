from django.contrib.auth.models import User
from rest_framework import serializers,validators
from .models import  *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'
        
        
        extra_kwargs={
            "password":{"write_only":True},
            "email":{
                "required":True,
                "allow_blank":False,
                "validators":{
                    validators.UniqueValidator(
                        User.objects.all(),"A user with that email already exists"
                    )
                }
                
            }
        }

def create(self, validated_data):
    username = validated_data.get('username')
    password = validated_data.get('password')
    email = validated_data.get('email')
    first_name = validated_data.get('first_name')
    last_name = validated_data.get('last_name')
    
    detail_obj = Details.objects.create(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name
    )
    
    return detail_obj