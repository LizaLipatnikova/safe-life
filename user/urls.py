from django.urls import path
from user.views import AuthWarningView, UserLoginView, RegistrationView, AccountView, UserLogoutView

urlpatterns = [
    path('warning/', AuthWarningView.as_view(), name="auth_warning"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('account/', AccountView.as_view(), name="account"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
]
