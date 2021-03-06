from django.urls import path, re_path
from django.conf.urls import include
from users.views import dashboard, register

urlpatterns = [
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    re_path(r"^dashboard/", dashboard, name="dashboard"),
    re_path(r"^register/", register, name="register"),
]