from django.conf.urls import url
from django.contrib import admin

# from rest_framework.authtoken import views

from accounts import views

urlpatterns = [
#USERS
  url(r'^users/$', views.UserListAPIView.as_view(), name=views.UserListAPIView.name),
  url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetailAPIView.as_view(), name=views.UserListAPIView.name),
#SUBSCRIBERS
  url(r'^register/$', views.SubscriberCreateAPIView.as_view(), name=views.SubscriberCreateAPIView.name),
  url(r'^subscribers/$', views.SubscriberListAPIView.as_view(), name=views.SubscriberListAPIView.name),
  url(r'^subscribers/(?P<pk>[0-9]+)/$', views.SubscriberDetailAPIView.as_view(), name=views.SubscriberDetailAPIView.name),
#TEAMS
  url(r'^team-create/$', views.TeamCreateAPIView.as_view(), name=views.TeamCreateAPIView.name),
  url(r'^teams/$', views.TeamListAPIView.as_view(), name=views.TeamListAPIView.name),
  url(r'^teams/(?P<pk>[0-9]+)/$', views.TeamDetailAPIView.as_view(), name=views.TeamDetailAPIView.name),
#COMPANIES
  url(r'^company-create/$', views.CompanyCreateAPIView.as_view(), name=views.CompanyCreateAPIView.name),
  url(r'^companies/$', views.CompanyListAPIView.as_view(), name=views.CompanyListAPIView.name),
  url(r'^companies/(?P<pk>[0-9]+)/$', views.CompanyDetailAPIView.as_view(), name=views.CompanyDetailAPIView.name),
#RELATIONS
  url(r'^teams-relations-create/$', views.TeamTreeCreateAPIView.as_view(), name=views.TeamTreeCreateAPIView.name),
  url(r'^teams-relations-list/$', views.TeamTreeAPIView.as_view(), name=views.TeamTreeAPIView.name),

  url(r'^team-subscriber-relations-create/$', views.TeamSubscriberCreateAPIView.as_view(), name=views.TeamSubscriberCreateAPIView.name),
  url(r'^team-subscriber-relations-list/$', views.TeamSubscriberAPIView.as_view(), name=views.TeamSubscriberAPIView.name),

  url(r'^company-subscriber-relations-create/$', views.CompanySubscriberCreateAPIView.as_view(), name=views.CompanySubscriberCreateAPIView.name),
  url(r'^company-subscriber-relations-list/$', views.CompanySubscriberAPIView.as_view(), name=views.CompanySubscriberAPIView.name),

  url(r'^company-team-relations-create/$', views.CompanyTeamCreateAPIView.as_view(), name=views.CompanyTeamCreateAPIView.name),
  url(r'^company-team-relations-list/$', views.CompanyTeamAPIView.as_view(), name=views.CompanyTeamAPIView.name),



]