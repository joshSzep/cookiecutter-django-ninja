# List available recipes
default:
    @just --list

# Install all dependencies
install:
    uv sync

# Run the development server
serve:
    uv run python src/backend/manage.py runserver

# Run tests with coverage
test:
    uv run pytest --cov=src/backend

# Run type checking
typecheck:
    uv run pyright

# Format code
fmt:
    uv run ruff format .

lint:
    uv run ruff check --fix .

# Run all checks (format, lint, type, tests)
check: fmt lint typecheck test

# Create and run migrations
migrate:
    uv run python src/backend/manage.py migrate

# Make migrations
makemigrations:
    uv run python src/backend/manage.py makemigrations

# Create a superuser
createsuperuser:
    uv run python src/backend/manage.py createsuperuser

# Clean python cache files
clean:
    find . -type d -name "__pycache__" -exec rm -r {} +
    find . -type f -name "*.pyc" -delete
    find . -type f -name "*.pyo" -delete
    find . -type f -name "*.pyd" -delete
    find . -type f -name ".coverage" -delete
    find . -type d -name "*.egg-info" -exec rm -r {} +
    find . -type d -name "*.egg" -exec rm -r {} +
    find . -type d -name ".pytest_cache" -exec rm -r {} +
    find . -type d -name ".ruff_cache" -exec rm -r {} +
