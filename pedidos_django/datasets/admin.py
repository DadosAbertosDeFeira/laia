from django.contrib import admin
from public_admin.sites import PublicAdminSite
from personal.models import RegistroPedidos

# class RegistroPedidosAdmin(PublicAdminSite):
#     pass


admin.site.register(RegistroPedidos)
# public_admin.register('', RegistroPedidosAdmin)