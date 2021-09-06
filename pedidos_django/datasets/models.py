from django.db import models

STATUS_OPTIONS = (
    ("SEM RESPOSTA"),
    ("RESPONDIDO PARCIALMENTE"),
    ("RESPONDIDO"),
    ("RESPONDIDO APÓS RECURSO"),
    ("EM RECURSO"),
    ("EM ANDAMENTO"),
    ("RESPONDIDO COM ATRASO"),
    ("PEDIDO NÃO PROCESSADO")
)

MUNICIPAL_OPTIONS = (
    ("SIM"),
    ("NÃO")
)

class RegistroPedidos(models.Model):
    data_envio = models.DateTimeField("Data de envio", db_index=True)
    data_resposta = models.DateTimeField("Data de resposta", db_index=True)
    dias_sem_resposta = models.IntegerField("Dias sem resposta", db_index=True)
    orgao = models.CharField("Órgão", max_length=50, blank=True)
    municipal = models.CharField("Municipal?", max_length=1, choices=MUNICIPAL_OPTIONS)
    meio_de_contato = models.TextField("Meio de Contato", null=True, blank=True)
    descricao_pedido = models.TextField("Descrição do Pedido", null=True, blank=True)
    status_pedido = models.CharField("Status do Pedido", max_length=1, choices=STATUS_OPTIONS, blank=True)
    historico_pedido = models.TextField("Historico", null=True, blank=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

