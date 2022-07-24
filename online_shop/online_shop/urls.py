from django.contrib import admin
from django.urls import include, path

api_urls = [
    path("", include("products.urls")),
    path("", include("users.urls")),
    path("", include("token_jwt.urls")),
    path("", include("orders.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urls)),
]
