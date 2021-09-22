from datetime import date

from django.contrib import admin
from public_admin.sites import PublicAdminSite, PublicApp

from pedidos.models import Orgao, Pedido


@admin.register(Pedido)
class PedidoModelAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "orgao",
        "status",
        "data_envio",
        "data_resposta",
        "dias_sem_resposta",
    )

    def dias_sem_resposta(self, pedido):
        diferenca = date.today() - pedido.data_envio
        return diferenca.days


class PublicPedidoModelAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "orgao",
        "status",
        "data_envio",
        "data_resposta",
        "dias_sem_resposta",
    )
    list_filter = (
        "status",
        "orgao__esfera",
    )

    def dias_sem_resposta(self, pedido):
        if pedido.data_resposta == None:
            diferenca = date.today() - pedido.data_envio
        else:
            diferenca = pedido.data_resposta - pedido.data_envio
        
        return diferenca.days


class PedidoPublicAdminSite(PublicAdminSite):
    site_title = "Pedidos de Informação"
    site_header = "Pedidos de Informação"
    index_title = "Dashboard"


@admin.register(Orgao)
class OrgaoModelAdmin(admin.ModelAdmin):
    pass


public_app = PublicApp("pedidos", models=("pedido",))
public_admin = PedidoPublicAdminSite(public_apps=public_app)
public_admin.register(Pedido, PublicPedidoModelAdmin)
