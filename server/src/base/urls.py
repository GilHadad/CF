from django.conf.urls import url
from django.contrib import admin

# from rest_framework.authtoken import views

from .views import ProductListView, ProductDetailAPIView

urlpatterns = [
    url(r'^project-list/$', ProductListView.as_view(), name='project-list'),
    url(r'^task-list/$', ProductListView.as_view(), name='task-list'),
]