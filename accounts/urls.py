from django.urls import path, re_path

from .views import (
        AccountHomeView, 
        AccountEmailActivateView,
        UserDetailUpdateView,
        )
app_name = 'account'
urlpatterns = [
    path('', AccountHomeView.as_view(), name='home'),
#     path('userdetail/', UserDetailUpdateView.as_view(), name='user-update'),
    path('userdetail/', UserDetailUpdateView, name='user-update'),
    re_path(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', 
            AccountEmailActivateView.as_view(), 
            name='email-activate'),
    path('email/resend-activation/', 
            AccountEmailActivateView.as_view(), 
            name='resend-activation'),
]

# account/email/confirm/asdfads/ -> activation view