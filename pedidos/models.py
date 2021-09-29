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

COMPLAINT_STATUS = (
    ("nova", "NOVA"),
    ("em_andamento", "EM ANDAMENTO"),
    ("deferida", "DEFERIDA"),
    ("indeferida", "INDEFERIDA"),
    ("arquivada", "ARQUIVADA"),
)

SPHERE_OPTIONS = (
    ("municipal", "MUNICIPAL"),
    ("estadual", "ESTADUAL"),
    ("federal", "FEDERAL"),
)


class Request(models.Model):
    num_protocol = models.CharField("Número de Protocolo", max_length=25, blank=True)
    sent_at = models.DateField("Data de envio", db_index=True)
    replied_at = models.DateField(
        "Data de resposta", db_index=True, null=True, blank=True
    )
    body = models.ForeignKey("Body", on_delete=models.PROTECT)
    title = models.CharField("Título do Pedido", max_length=100)
    means_of_contact = models.CharField("Meio de Contato", max_length=200)
    status = models.CharField(
        "Status do Pedido", max_length=50, choices=STATUS_OPTIONS, blank=True
    )
    historic = models.TextField("Historico", null=True, blank=True)
    text = models.TextField("Texto")
    reply = models.TextField("Resposta", null=True, blank=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return self.title


class Body(models.Model):
    name = models.CharField("Nome", max_length=100, blank=True)
    initials = models.CharField("Sigla", max_length=50, blank=True)
    sphere = models.CharField("Esfera", max_length=20, choices=SPHERE_OPTIONS)
    website = models.URLField("Site", max_length=50, blank=True)
    email = models.EmailField("E-mail", blank=True)
    telephone_number = models.CharField("Telefone", max_length=50, blank=True)
    extra_information = models.TextField(
        "Informações adicionais sobre o órgão", null=True, blank=True
    )

    class Meta:
        verbose_name = "Órgão"
        verbose_name_plural = "Órgãos"

    def __str__(self):
        return self.initials


class Complaint(models.Model):
    request = models.ForeignKey("Request", on_delete=models.PROTECT)
    created_at = models.DateField("Data de criação", db_index=True)
    finished_at = models.DateField(
        "Data de conclusão", db_index=True, null=True, blank=True
    )
    title = models.CharField("Título", max_length=100)
    body = models.ForeignKey("Body", on_delete=models.PROTECT)
    means_of_contact = models.CharField("Meio de Contato", max_length=200)
    status = models.CharField(
        "Status", max_length=50, choices=COMPLAINT_STATUS, blank=True
    )
    text = models.TextField("Texto")
    historic = models.TextField("Historico", null=True, blank=True)
    reply = models.TextField("Resposta", null=True, blank=True)
    extra_information = models.TextField(
        "Observações adicionais da denúncia", null=True, blank=True
    )

    class Meta:
        verbose_name = "Denúncia"
        verbose_name_plural = "Denúncias"

    def __str__(self):
        return f"{self.title} ({self.request.body} | {self.body})"
