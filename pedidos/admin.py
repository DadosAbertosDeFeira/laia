from datetime import date

from django.conf import settings
from django.contrib import admin
from public_admin.sites import PublicAdminSite, PublicApp

from pedidos.models import Body, Complaint, Request


class RequestMixin(admin.ModelAdmin):
    list_display = (
        "title",
        "body",
        "status",
        "sent_at",
        "replied_at",
        "days_without_reply",
    )

    def days_without_reply(self, request):
        if request.replied_at is None:
            difference = date.today() - request.sent_at
        else:
            difference = request.replied_at - request.sent_at

        return difference.days


class PublicRequestModelAdmin(RequestMixin, admin.ModelAdmin):
    list_filter = (
        "status",
        "body__sphere",
    )


class RequestPublicAdminSite(PublicAdminSite):
    organization = (
        f" - {settings.ORGANIZATION_NAME}" if settings.ORGANIZATION_NAME else ""
    )
    site_title = f"Pedidos de Informação {organization}"
    site_header = f"Pedidos de Informação {organization}"
    index_title = "Dashboard"


@admin.register(Request)
class RequestModelAdmin(RequestMixin, admin.ModelAdmin):
    pass


@admin.register(Body)
class BodyModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Complaint)
class ComplaintModelAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "body",
        "request_and_body",
        "status",
        "created_at",
        "finished_at",
    )
    list_filter = (
        "status",
        "body__sphere",
    )

    def request_and_body(self, obj):
        return f"{obj.request.title} ({obj.request.body.initials})"

    request_and_body.short_description = "Pedido"


public_app = PublicApp("pedidos", models=("request", "complaint"))
public_admin = RequestPublicAdminSite(public_apps=public_app)
public_admin.register(Request, PublicRequestModelAdmin)
public_admin.register(Complaint, ComplaintModelAdmin)
