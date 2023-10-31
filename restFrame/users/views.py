from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer
from .models import *

@api_view(['POST'])
def login_api(request):

    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    detail_obj = serializer.validated_data['detail_obj ']
    created, token = AuthToken.objects.create(detail_obj )
    
    return Response({
        'user_info':{
            'id':detail_obj .id,
            'username':detail_obj .username,
            'email':detail_obj .email    
        },
        'token':token
    })
#read    
@api_view(['GET'])
def home_api(request):
    detail_obj = Details.objects.all()
    serializer = RegisterSerializer(detail_obj,many=True)  
    return Response(serializer.data)

# @api_view(['GET'])
# def get_user_data(request):
#     detail_obj = Details.objects.all()
#     if detail_obj.is_authenticated:
#         return Response({
#              'user_info':{
#              'id':detail_obj.id,
#              'username':detail_obj.username,
#              'email':detail_obj.email    
#              },
#         })  
#     return Response({'error': 'not authenticated'},status=400) 
        
    
@api_view(['POST'])
def register_api(request):
    detail_obj = Details.objects.all()
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
       serializer.save()
    return Response(serializer.data)