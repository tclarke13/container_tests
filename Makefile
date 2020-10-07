build:
	docker-compose build container-tests

run: build
	docker-compose run --rm test-container-time

