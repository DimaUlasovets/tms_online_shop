from django.urls import include, path
from users.api.v1.endpoints.auth import LogoutView, SignInView, SignUpView

auth_urlpatterns = [
    path("signup/", SignUpView.as_view()),
    path("signin/", SignInView.as_view()),
    path("logout/", LogoutView.as_view()),
]


urlpatterns = [
    path("users/auth/", include(auth_urlpatterns)),
]
