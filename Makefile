# Makefile - NextGenHealth
#
# Usage:
#   make test        → Run all unit tests in user_management domain
#   make coverage    → Run tests with coverage report (terminal + HTML)
#   make setup       → Install dependencies

# Run ALL unit tests in the domain layer
test:
	python -m pytest tests/unit/user_management/domain/ -v

# Run tests with coverage report (console and HTML)
coverage: ensure-cov
	python -m pytest \
		--cov=src/user_management \
		--cov-report=term \
		--cov-report=html:coverage_html \
		--cov-config=.coveragerc \
		tests/unit/user_management/domain/user/

ensure-cov:
	@echo "🔍 Checking virtual environment..."
	@if ! python -c "import pytest_cov" 2>/dev/null; then \
		echo "⚠️ Installing pytest-cov..."; \
		pip install pytest-cov; \
	else \
		echo "✅ pytest-cov is installed"; \
	fi

# Install dependencies
setup:
	pip install -r requirements.txt

# Clean generated files
clean:
	rm -rf build/ dist/ *.egg-info/
	rm -rf .pytest_cache/ .coverage
	rm -rf coverage_html/

.PHONY: test setup coverage clean