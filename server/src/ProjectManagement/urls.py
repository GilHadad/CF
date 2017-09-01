from django.conf.urls import url
from django.contrib import admin

from .views import ProjectListView, TaskListView

urlpatterns = [
    url(r'^ProjectList/$', ProjectListView.as_view(), name='ProjectList'),
    url(r'^TaskList/$', TaskListView.as_view(), name='TaskList'),
]