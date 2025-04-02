from django.urls import path
from .views import LoginView, ForgotPasswordView, ResetPasswordView

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("forgot-password/", ForgotPasswordView.as_view(), name="forgot_password"),
    path("reset-password/<str:uidb64>/<str:token>/", ResetPasswordView.as_view(), name="reset-password"),
]
