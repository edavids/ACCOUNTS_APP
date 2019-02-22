"""frank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

#ACCOUNT VIEW IMPORTS
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView, RedirectView
from accounts.views import LoginView, RegisterView#, StaffRegisterView

from django.contrib import admin
from django.urls import path, include

from .views import home, contact_page, success

urlpatterns = [
    path('admin/', admin.site.urls),

    #ACCOUNT LINKS AND PASSWORD(LOGIN & LOGOUT)
    path('accounts/', RedirectView.as_view(url='/account')),
    path('account/', include("accounts.urls", namespace='account')),
    path('accounts/', include("accounts.passwords.urls")),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('register/staff', StaffRegisterView.as_view(), name='staff-register'),

    path('', home, name='home'),
    path('contact/', contact_page, name='contact'),
    path('contact/success', success, name='email-success'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)