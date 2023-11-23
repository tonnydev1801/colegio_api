#Serializer created by: Antonio González, antonioglez1801@gmail.com

from rest_framework import serializers
from users.models import User


#Create UserSerializer for the model User
class UserSerializer( serializers.ModelSerializer ):
    #Meta class for UserSerializer
    class Meta:
        model = User
        fields = [ 'id', 'first_name', 'last_name', 'username', 'email', 'password', 'is_teacher', 'is_student' ]
    
    #Encrypt the user password, overriding the create method
    def create( self, validated_data ):
        #Adding a password validation
        password = validated_data.pop( 'password', None )
        instance = self.Meta.model( **validated_data )
        #If the password is not None, encrypt it
        if password is not None:
            instance.set_password( password )
        instance.save()
        return instance


#Create a serializer for get the data of the authenticated user
class UserSerializerStaffAuth( serializers.ModelSerializer ):
    class Meta:
        model = User
        fields = [ 'id', 'username', 'email', 'first_name', 'last_name', 'is_teacher', 'is_student' ]
