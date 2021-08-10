docker-build:
	docker build -t wagtail_starter_project:latest ./src

docker-start:
	cd ./src && docker-compose up --remove-orphans $(options)

docker-stop:
	cd ./src && docker-compose down --remove-orphans $(options)
	docker rmi wagtail_starter_project:latest

docker-shell:
	cd ./src && docker-compose run --rm $(options) website /bin/bash

docker-migrations:
	cd ./src && docker-compose run --rm $(options) website python manage.py makemigrations
	cd ./src && docker-compose run --rm $(options) website python manage.py migrate

docker-superuser:
	cd ./src && docker-compose run --rm $(options) website python manage.py createsuperuser
