from django.contrib import admin
from public_admin.sites import PublicAdminSite, PublicApp

from pedidos.models import Pedido


@admin.register(Pedido)
class PedidoModelAdmin(admin.ModelAdmin):
    pass


class PublicPedidoModelAdmin(admin.ModelAdmin):
    list_display = (
        "data_envio",
        "titulo",
        "orgao",
    )
    list_filter = ("status",)


class PedidoPublicAdminSite(PublicAdminSite):
    site_title = "Pedidos de Informação"
    site_header = "Pedidos de Informação"
    index_title = "Dashboard"


public_app = PublicApp("pedidos", models=("pedido",))
public_admin = PedidoPublicAdminSite(public_apps=public_app)
public_admin.register(Pedido, PublicPedidoModelAdmin)
