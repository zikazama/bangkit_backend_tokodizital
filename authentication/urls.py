from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authentication.views.user_view import UserRegistration, UserLogin, EditProfile, LoggedinUser
from authentication.views.user_reset_view import ResetPassword

urlpatterns = [

    path('register/', UserRegistration.as_view()),
    path('login/', UserLogin.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('reset-password/', ResetPassword.as_view()),
    path('edit-profile/', EditProfile.as_view()),
    path('user/', LoggedinUser.as_view()),


]
