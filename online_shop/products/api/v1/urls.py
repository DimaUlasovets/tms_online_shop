from django.urls import path
from products.api.v1 import endpoints
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("products/", endpoints.ProductList.as_view(), name="products_list_api"),
    path("products/<uuid:pk>", endpoints.ProductDetail.as_view(), name="products_detail_api"),
    path("categorys/", endpoints.CategoryList.as_view(), name="categorys_list_api"),
    path("categorys/<uuid:pk>", endpoints.CategoryDetail.as_view(), name="categorys_detail_api"),
    path("brands/", endpoints.BrandList.as_view(), name="brands_list_api"),
    path("brands/<uuid:pk>", endpoints.BrandDetail.as_view(), name="brands_detail_api"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
