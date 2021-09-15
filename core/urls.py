from django.contrib import admin
from django.urls import path

from pedidos.admin import public_admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", public_admin.urls),
]
