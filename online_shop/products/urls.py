from django.conf.urls import include
from django.urls import re_path

urlpatterns = [re_path(r"v1/", include("products.api.v1.urls"))]
