from django.conf import settings
from django.contrib import admin
from public_admin.sites import PublicAdminSite, PublicApp

from information_requests.models import Complaint, InformationRequest, PublicAgency


class InformationRequestMixin(admin.ModelAdmin):
    list_display = (
        "title",
        "public_agency",
        "status",
        "sent_at",
        "replied_at",
        "days_without_reply",
    )

    def days_without_reply(self, information_request):
        return information_request.days_without_reply

    days_without_reply.short_description = "Dias sem resposta"


class PublicRequestModelAdmin(InformationRequestMixin, admin.ModelAdmin):
    list_filter = (
        "status",
        "public_agency__sphere",
    )


class RequestPublicAdminSite(PublicAdminSite):
    organization = (
        f" - {settings.ORGANIZATION_NAME}" if settings.ORGANIZATION_NAME else ""
    )
    site_title = f"Pedidos de Informação {organization}"
    site_header = f"Pedidos de Informação {organization}"
    index_title = "Dashboard"


@admin.register(InformationRequest)
class InformationRequestModelAdmin(InformationRequestMixin, admin.ModelAdmin):
    pass


@admin.register(PublicAgency)
class BodyModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Complaint)
class ComplaintModelAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "public_agency",
        "request_and_body",
        "status",
        "created_at",
        "finished_at",
    )
    list_filter = (
        "status",
        "public_agency__sphere",
    )

    def request_and_body(self, obj):
        public_agency_initials = obj.information_request.public_agency.initials
        return f"{obj.information_request.title} ({public_agency_initials})"

    request_and_body.short_description = "Pedido"


public_app = PublicApp(
    "information_requests", models=("informationrequest", "complaint")
)
public_admin = RequestPublicAdminSite(public_apps=public_app)
public_admin.register(InformationRequest, PublicRequestModelAdmin)
public_admin.register(Complaint, ComplaintModelAdmin)
admin.site.disable_action("delete_selected")
