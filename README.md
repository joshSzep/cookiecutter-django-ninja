# cookiecutter-django-ninja

A modern, high-performance Django template using django-ninja for building REST APIs.

## Features

- Built with Python 3.13+ and Django 5.1+
- High-performance REST API using django-ninja 1.3+
- Real-time WebSocket support:
  - Built-in WebSocket example with time broadcasting
  - Async WebSocket consumers using channels
  - Clean WebSocket routing configuration
- Modern async support with uvicorn and gunicorn
- Modern dependency management:
  - `uv` for fast, reliable Python package management
  - Strict dependency locking with `uv.lock`
- Comprehensive code quality tools:
  - Ruff for fast linting and formatting
  - Pyright for static type checking
  - Pre-commit hooks for consistent code quality
  - Pytest with coverage reporting and async support
  - CI/CD ready with GitHub Actions
- Modern Python features:
  - Full type hinting with latest Python 3.13 syntax
  - Async/await support throughout
  - Modern import style (no relative imports)
  - PEP-compliant code formatting
- Structured project layout following Django best practices
- Production-ready ASGI configuration

## Requirements

- Python 3.13 or higher
- `uv` package manager
- Git for version control
- Pre-commit (optional, but recommended)

## Project Structure

```text
├── src/
│   └── backend/             # Main Django project directory
│       ├── api/             # API application
│       │   ├── api.py       # Main API router
│       │   ├── consumers.py # WebSocket consumers
│       │   └── routing.py   # WebSocket routing
│       └── project/         # Project configuration
│           ├── settings.py
│           ├── urls.py
│           └── asgi.py
├── test/                    # Test directory
│   ├── conftest.py         # Test configuration
│   └── api/                # API tests
├── pyproject.toml          # Project dependencies and tools configuration
├── uv.lock                 # Locked dependencies
├── justfile                # Development commands
├── gunicorn.conf.py        # Gunicorn server configuration
└── .pre-commit-config.yaml # Pre-commit hooks configuration
```

## Development Setup

### Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` file with your specific configuration values.

### Install dependencies

```bash
just install
```

### Set up pre-commit hooks (recommended)

```bash
just pre-commit
```

### Run migrations

```bash
just migrate
```

### Start development server

```bash
just serve
```

## Development Commands

The project uses `just` for common development tasks:

- `just install` - Install all dependencies
- `just serve` - Start development server
- `just test` - Run tests
- `just lint` - Run linting
- `just format` - Format code
- `just check` - Run all checks (types, lint, format)
- `just migrate` - Run database migrations
- `just pre-commit` - Install pre-commit hooks

## Example Endpoints

### REST API

- `/api/health` - Health check endpoint
- `/api/docs` - Interactive API documentation (Swagger UI)

### WebSocket

- `/ws/time/` - WebSocket endpoint that broadcasts current time every second
- `/api/websocket-test` - Test page for WebSocket time broadcast

## Code Quality

This project enforces high code quality standards:

- Type checking with pyright
- Linting and formatting with Ruff
- Automated testing with pytest
- Pre-commit hooks for consistent code quality
- Modern Python type hints throughout
- No relative imports
- Single-line imports for better git diffs
- 88-character line length limit

## API Development

The project uses django-ninja for building REST APIs:

- Type-safe request/response validation
- Automatic OpenAPI/Swagger documentation
- Built-in authentication support
- High performance with async support
- Easy to test with pytest-asyncio

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and checks (`just check && just test`)
5. Commit your changes
6. Push to your branch
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
