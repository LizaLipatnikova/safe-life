from django.urls import path
from user.views import *

urlpatterns = [
    path('warning/', AuthWarningView.as_view(), name="auth_warning"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('account/', AccountView.as_view(), name="account"),
    path('account/edit/<int:pk>/', AccountEditView.as_view(), name="account_edit"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
]
