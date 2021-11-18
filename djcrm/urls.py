"""djcrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from core.views import TestView, LeadTestView, PostCreateAPI, PostGetAPI
from rest_framework.authtoken.views import obtain_auth_token
from leads.views import landing_page, LandingTemplateView, SignupView

urlpatterns = [
    path('', LandingTemplateView.as_view(), name='landing-page'),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace='leads')),
    path('agents/', include('agents.urls', namespace='agents')),
    path('core/', TestView.as_view(), name='test'),
    path('core/get/', PostGetAPI.as_view(), name='get-post-api-test'),
    path('core/post/', PostCreateAPI.as_view(), name='create-post-api-test'),
    path('lead/test/', LeadTestView.as_view(), name='lead-api'),
    path('user/token/', obtain_auth_token, name='obtain-token'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
