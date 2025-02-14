# cookiecutter-django-ninja

A modern, high-performance Django template using django-ninja for building REST APIs.

## Features

- Built with Python 3.13+ and Django 5.1+
- REST API using django-ninja 1.3+
- Modern dependency management with `uv`
- Comprehensive code quality tools:
  - Ruff for linting and formatting
  - Pyright for static type checking
  - Pre-commit hooks
  - Pytest with coverage reporting
- Structured project layout following Django best practices

## Requirements

- Python 3.13 or higher
- `uv` package manager

## Project Structure

```
src/
├── backend/           # Main Django project directory
│   ├── api/          # API application
│   └── project/      # Project configuration
test/                 # Test directory
```

## Quick Start

1. Install dependencies:
```bash
just install
```

2. Set up pre-commit hooks:
```bash
just pre-commit
```

3. Run migrations:
```bash
just migrate
```

4. Start development server:
```bash
just serve
```

## Development Commands

- `just serve` - Run development server
- `just test` - Run tests with coverage
- `just typecheck` - Run type checking
- `just fmt` - Format code
- `just lint` - Lint code
- `just migrate` - Apply database migrations
- `just makemigrations` - Create new migrations
- `just createsuperuser` - Create Django admin user
- `just clean` - Clean Python cache files

## Code Style

This project follows strict code style guidelines:
- Uses double quotes for strings
- 88 character line length limit
- Single imports per line
- Type annotations required
- Trailing commas in data structures
- Comprehensive static type checking with pyright

## License

This project is licensed under the MIT License - see the LICENSE file for details.
