SRC_DIR := orders_app
ALEMBIC_CONFIG ?= alembic.ini
ALEMBIC_CMD = PYTHONPATH=./ alembic -c $(ALEMBIC_CONFIG)
PORT ?= 8080

.PHONY: lint run auto up down his test test_cov

lint: ## 🔎 Lint & format
	@echo "Running lint checks..."
	. .venv/bin/activate && \
	black . $(SRC_DIR)/ && \
	flake8 $(SRC_DIR)/ && \
	isort $(SRC_DIR)/ && \
	mypy --explicit-package-bases $(SRC_DIR)/

run: ## 🏃 Run app
	@echo "Starting backend..."
	. .venv/bin/activate && export ENV=dev && uv run manage.py runserver

auto: ## 🎁 Create a new Alembic revision with autogenerate
	@echo "Creating new Alembic revision..."
	. .venv/bin/activate && $(ALEMBIC_CMD) revision --autogenerate -m "$(msg)"

up: ## ⬆️ Upgrade database to a specific revision or 'head'
	@echo "Upgrading database..."
	. .venv/bin/activate && $(ALEMBIC_CMD) upgrade $(rev)

down: ## ⬇️ Downgrade database to a specific revision or 'base'
	@echo "Downgrading database..."
	. .venv/bin/activate && $(ALEMBIC_CMD) downgrade $(rev)

his: ## 📋 Show the migration history
	@echo "Alembic migration history:"
	. .venv/bin/activate && $(ALEMBIC_CMD) history

test: ## 🧪 Run tests
	@echo "Starting pytesting..."
	. .venv/bin/activate && pytest -v

test_cov: ## 🧪 Run tests with coverage
	@echo "Starting pytesting with coverage..."
	. .venv/bin/activate && pytest -v --cov --cov-report=term-missing

