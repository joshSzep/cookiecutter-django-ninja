# List available recipes
default:
    @just --list

# Install all dependencies
install:
    uv sync

# Run the development server
serve:
    uv run gunicorn -c gunicorn.conf.py src.backend.project.asgi:application

# Run tests with coverage
test:
    uv run pytest --cov=src/backend

# Run type checking
typecheck:
    uv run pyright

# Format code
fmt:
    uv run ruff format .

# Lint code
lint:
    uv run ruff check --fix .

# Run the pre-commit checks
pre-commit:
    uv run pre-commit install
    uv run pre-commit run --all

# Create and run migrations
migrate:
    uv run python manage.py migrate

# Make migrations
makemigrations:
    uv run python manage.py makemigrations

# Create a superuser
createsuperuser:
    uv run python manage.py createsuperuser

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
