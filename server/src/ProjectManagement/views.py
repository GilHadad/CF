from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.shortcuts import render

from .api import ProjectSerializer, TaskSerializer
from .models import Project,Task

from rest_framework.permissions import BasePermission, SAFE_METHODS

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object.'
    # my_safe_method = ['GET', 'PUT']
    # def has_permission(self, request, view):
    #     if request.method in self.my_safe_method:
    #         return True
    #     return False

    def has_object_permission(self, request, view, obj):
        #member = Membership.objects.get(user=request.user)
        #member.is_active
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user




###############
# ListAPIView #
###############

class ProjectListView(ListAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  permission_classes = [IsAuthenticated] #needs to be updated!!!
  

class TaskListView(ListAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  permission_classes = [IsAuthenticated] #needs to be updated!!!

#################
# DetailAPIView #
#################

class ProjectDetailAPIView(RetrieveAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  lookup_field = 'id'

class TaskDetailAPIView(RetrieveAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  lookup_field = 'id'

