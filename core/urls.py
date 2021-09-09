from django.contrib import admin
from django.urls import path
from pedidos.admin import public_admin


urlpatterns = [
    path("", public_admin.urls),
    path('admin/', admin.site.urls),
]
