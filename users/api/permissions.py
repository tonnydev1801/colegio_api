#Permissions created by: Antonio González, antonioglez1801@gmail.com

from rest_framework.permissions import BasePermission


#Custom permission for staff authenthicated users
class IsStaffAuthenticated( BasePermission ):
    #Check if the user is staff
    def has_permission( self, request, view ):
        #If the user is staff, return True
        if request.user.is_staff:
            return True
        #If the user is not staff, return False
        return False