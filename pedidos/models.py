from django.db import models

STATUS_OPTIONS = (
    ("sem_resposta", "SEM RESPOSTA"),
    ("respondido_parcialmente", "RESPONDIDO PARCIALMENTE"),
    ("respondido", "RESPONDIDO"),
    ("respondido_apos_recurso", "RESPONDIDO APÓS RECURSO"),
    ("em_recurso", "EM RECURSO"),
    ("em_andamento", "EM ANDAMENTO"),
    ("respondido_com_atraso", "RESPONDIDO COM ATRASO"),
    ("pedido_nao_processado", "PEDIDO NÃO PROCESSADO"),
)

ESFERA_OPTIONS = (
    ("municipal", "MUNICIPAL"),
    ("estadual", "ESTADUAL"),
    ("federal", "FEDERAL"),
)


class Pedido(models.Model):
    num_protocolo = models.CharField("Número de Protocolo", max_length=25, blank=True)
    data_envio = models.DateField("Data de envio", db_index=True)
    data_resposta = models.DateField(
        "Data de resposta", db_index=True, null=True, blank=True
    )
    orgao = models.CharField("Órgão", max_length=50, blank=True)
    esfera = models.CharField("Esfera", max_length=20, choices=ESFERA_OPTIONS)
    titulo = models.CharField("Título do Pedido", max_length=100)
    meio_de_contato = models.CharField("Meio de Contato", max_length=200)
    status = models.CharField(
        "Status do Pedido", max_length=50, choices=STATUS_OPTIONS, blank=True
    )
    historico = models.TextField("Historico", null=True, blank=True)
    texto = models.TextField("Texto")
    resposta = models.TextField("Resposta", null=True, blank=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return self.titulo
