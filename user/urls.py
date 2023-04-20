from django.urls import path

from django.contrib.auth.views import LogoutView
from .views import *

from .password_views import *

from django.conf import settings

app_name = 'user'

urlpatterns = [

    # Auth
    path('login/', log_in, name = 'login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name = 'logout'),
    path('register/', register, name = 'register'),
    path('register/<str:premium_invite_uid>/', invited_register, name = 'invited-register'),

    # Reset Password
    path('forgot-password/', forgot_password, name = 'forgot-password'),
    path('recover-password/', recover_password, name = 'recover-password'),
    path('reset-password/<uuid:uid>/', reset_password, name = 'reset-password'),

    path('confirm-email/', ce, name = 'ce'), # Email confirmation

    path('toggle-mode/', toggle_mode, name = 'toggle-mode'), # Dark/light

    # Account info
    path('cn/', change_name, name = 'cn'),
    path('cu/', change_username, name = 'cu'),
    path('cp/', change_password, name = 'cp'),

]