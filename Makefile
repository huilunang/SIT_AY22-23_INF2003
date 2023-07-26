build:
	@echo "Building Docker containers..."
	docker-compose build
	docker image prune -f

up:
	@echo "Starting Docker containers..."
	docker-compose up -d

down:
	@echo "Stopping Docker containers..."
	docker-compose down

logs:
	@echo "Viewing Docker container logs..."
	docker-compose logs -f

clean: down
	@echo "Removing application containers and volumes..."
	docker-compose rm -v
	docker volume prune -f

# Entrypoint to run services
run: clean build up logs
	@echo "App is accesible at http://127.0.0.1:5000/..."

deepclean:
	@echo "Removing all resources..."
	docker system prune
