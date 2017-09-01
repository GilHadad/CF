from django.contrib.auth.models import User
from rest_framework import permissions

from accounts.models import *

def get_subscriber(user):
  user_id = user.id
  subscriber = Subscriber.objects.get(user=user_id)
  return subscriber


class IsInCompany(permissions.BasePermission):
  message = 'Adding customers not allowed'
  def has_permission(self, request, view):
      all_subscribers = CompanySubscriber.objects.all()
      
      return True

    

class IsInRelatedGroups(permissions.BasePermission):
   pass

class IsGroupManager(permissions.BasePermission):
    pass

class IsInGroup(permissions.BasePermission):
    pass

class IsOwner(permissions.BasePermission):
  pass



