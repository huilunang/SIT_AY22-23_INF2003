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

# Entrypoint to run services
run: down build up logs
	@echo "App is accesible at http://127.0.0.1:5000/..."

clean: down
	@echo "Removing application containers and volumes..."
	docker-compose rm -v

deepclean: clean
	@echo "Removing unused resources..."
	docker image prune -f
	docker volume prune -f
