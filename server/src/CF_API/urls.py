"""CF_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

# from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework_jwt.views import refresh_jwt_token
# from rest_framework_jwt.views import verify_jwt_token


from base.views import ProductListView
from ProjectManagement.views import ProjectListView, TaskListView



urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # API Base
    url(r'^api-base/products$', ProductListView.as_view(), name='get_get_products'),

    # API Accounts
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api-accounts/', include("accounts.urls", namespace='accounts-api')),

    # JWT
    # url(r'^api-auth-token/', obtain_jwt_token),
    # url(r'^api-token-refresh/', refresh_jwt_token),
    # url(r'^api-token-verify/', verify_jwt_token),

    # API ProjectManagement
    #url(r'^api/ProjectManagement/ProjectList$', ProjectListView.as_view(), name='get-ProjectList'),
    #url(r'^api/ProjectManagement/TaskList$', TaskListView.as_view(), name='get-TaskList'),
    # url(r'^api-ProjectManagement/', include("ProjectManagement.urls", namespace='ProjectManagement-api')),
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
