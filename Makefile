bash:
	docker-compose run --rm web bash

build:
	docker-compose build

createsuperuser:
	docker-compose run --rm web python manage.py createsuperuser

makemigrations:
	docker-compose run --rm web python manage.py makemigrations

migrate:
	docker-compose run --rm web python manage.py migrate

run:
	docker-compose up -d

stop:
	docker-compose stop

shell:
	docker-compose run --rm web python manage.py shell
