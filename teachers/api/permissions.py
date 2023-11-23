#Permissions created by: Antonio González, antonioglez1801@gmail.com
from rest_framework.permissions import BasePermission


#Custom permission to allow only admin to create, update and delete
class IsStaffOrReadOnly( BasePermission ):
    #Override has_permission method
    def has_permission( self, request, view ):
        #If request method == GET the user can read
        if request.method == 'GET':
            return True
        else:
            #If user is admin, he can do anything
            if request.user.is_staff:
                return True
            else:
                return False