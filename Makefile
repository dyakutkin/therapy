run:
	docker-compose up
test:
	docker exec therapy_webapp python -m unittest
coverage:
	docker exec therapy_webapp coverage run -m unittest
	docker exec therapy_webapp coverage report