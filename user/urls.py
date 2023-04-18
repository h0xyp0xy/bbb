from django.urls import path

from django.contrib.auth.views import LogoutView
from .views import *

from django.conf import settings

app_name = 'user'

urlpatterns = [

    # Auth
    path('login/', log_in, name = 'login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name = 'logout'),
    path('register/', register, name = 'register'),
    path('register/<str:premium_invite_uid>/', invited_register, name = 'invited-register'),

    #OAuth2

    path('confirm-email/', ce, name = 'ce'), # Email confirmation

    path('toggle-mode/', toggle_mode, name = 'toggle-mode'), # Dark/light

    # Account info
    path('cn/', change_name, name = 'cn'),
    path('cu/', change_username, name = 'cu'),
    path('cp/', change_password, name = 'cp'),

]