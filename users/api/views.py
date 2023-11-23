#View created by: Antonio González, antonioglez1801@gmail.com

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import UserSerializer, UserSerializerStaffAuth
from users.api.permissions import IsStaffAuthenticated

#Register class view
class RegisterUser( APIView ):
    #Override the post method for create admin users
    def post( self, request ):
        #Set the serializer with the data from the request
        serializer = UserSerializer( data=request.data )
        #Validate the serializer
        if serializer.is_valid( raise_exception=True ):
            serializer.save()
            return Response( status=status.HTTP_201_CREATED, data=serializer.data )
        #If the serializer is not valid, return a bad request
        return Response( status=status.HTTP_400_BAD_REQUEST, data=serializer.errors )


class AuthUser( APIView ):
    #If is an authenticated user, return the user data
    permission_classes = [ IsStaffAuthenticated ]
    #Override the get method for retrieve the user data
    def get( self, request ):
        #Set the serializer with the data from the request
        serializer = UserSerializerStaffAuth( request.user )
        #Return the user data
        return Response( status=status.HTTP_200_OK, data=serializer.data )