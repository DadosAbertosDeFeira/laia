import csv
from django.core.management.base import BaseCommand
from information_requests.models import InformationRequest
from information_requests.models import PublicAgency
from dateutil.parser import parse


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("csvfile")

    def handle(self, *args, **options):

        count = 0
        with open(options.get("csvfile")) as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                public_agency, _ = PublicAgency.objects.get_or_create(
                    name = row["Nome do Órgão"],
                    initials = row["Sigla do Órgão"],
                    sphere = row["Esfera"].lower()
                )
                
                InformationRequest.objects.get_or_create(
                    sent_at = parse(row["Data de envio"]),
                    replied_at = parse(row["Data de resposta"]) if row["Data de resposta"] else None,
                    public_agency = public_agency,
                    title = row["Pedido"],
                    contact = row["Meio de contato"],
                    status = row["Status"].lower().replace(" ", "_"),
                    historic = row["Histórico"],
                    text = row["Texto"],
                    reply = row["Resposta"],
                )
                count += 1

            self.stdout.write(self.style.SUCCESS(f"Concluído! Foram inseridos um total de {count} pedidos de informação."))
            
