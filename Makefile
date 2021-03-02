build:
	docker build -t wagtail_starter_project:latest ./src

compose-start: build
	cd ./src && docker-compose up

compose-stop:
	cd ./src && docker-compose down
	docker rmi wagtail_starter_project:latest

compose-shell:
	cd ./src && docker-compose run website /bin/bash

compose-py-migrations:
	cd ./src && docker-compose run website python manage.py makemigrations
	cd ./src && docker-compose run website python manage.py migrate

compose-py-superuser:
	cd ./src && docker-compose run website python manage.py createsuperuser
