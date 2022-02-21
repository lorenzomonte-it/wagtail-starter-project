.DEFAULT_GOAL := help

.PHONY: docker-build
docker-build:  ## Create docker-image
	docker build -t {{cookiecutter.project_slug}}:latest ./src

.PHONY: docker-start
docker-start:  ## Start docker-container with docker-image and database
	cd ./src && docker-compose up --remove-orphans $(options)

.PHONY: docker-stop
docker-stop:  ## Stop docker-container and remove docker-image
	cd ./src && docker-compose down --remove-orphans $(options)
	docker rmi {{cookiecutter.project_slug}}:latest

.PHONY: docker-shell
docker-shell:  ## Open shell inside docker-container
	cd ./src && docker-compose run --rm $(options) website /bin/bash

.PHONY: help
help:
	@echo "[Help] Makefile list commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
