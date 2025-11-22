#This allows specific actions from different user roles.
from rest_framework import permissions

#Only allow access to users with the 'agent' role
class IsAgent(permissions.BasePermission):
    def has_permission(self, request, view):
      return request.user.is_authenticated and request.user.role == 'agent'
  
class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'client'