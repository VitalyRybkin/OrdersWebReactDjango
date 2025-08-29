SRC_DIR := orders_app
ALEMBIC_CONFIG ?= alembic.ini
ALEMBIC_CMD = PYTHONPATH=./ alembic -c $(ALEMBIC_CONFIG)
PORT ?= 8080

.PHONY: lint run auto up down his test test_cov


YELLOW := \033[0;33m
GREEN := \033[0;32m
BOLD := \033[1m
NC := \033[0m # No Color (resets to default)

lint: ## 🔎 Lint & format
	@echo "Running lint checks..."
	. .venv/bin/activate && \
	black . $(SRC_DIR)/ && \
	flake8 $(SRC_DIR)/ && \
	isort $(SRC_DIR)/ && \
	mypy --explicit-package-bases $(SRC_DIR)/

run: ## 🏃 Run app
	@echo "${YELLOW}${BOLD}Starting backend...${NC}"
	. .venv/bin/activate && export ENV=dev && uv run manage.py runserver

migrate: ## ➡️ Apply all migrations
	@echo "${YELLOW}${BOLD}Starting migrations...${NC}"
	. .venv/bin/activate && export ENV=dev && uv run manage.py migrate
	@echo "${YELLOW}${BOLD}Done!${NC}"

migrations: ## 🔄 Make new migrations
	@echo "${YELLOW}${BOLD}Starting migrations...${NC}"
	. .venv/bin/activate && export ENV=dev && uv run manage.py makemigrations
	@echo "${YELLOW}${BOLD}Done!${NC}"

#auto: ## 🎁 Create a new Alembic revision with autogenerate
#	@echo "Creating new Alembic revision..."
#	. .venv/bin/activate && $(ALEMBIC_CMD) revision --autogenerate -m "$(msg)"
#
#up: ## ⬆️ Upgrade database to a specific revision or 'head'
#	@echo "Upgrading database..."
#	. .venv/bin/activate && $(ALEMBIC_CMD) upgrade $(rev)
#
#down: ## ⬇️ Downgrade database to a specific revision or 'base'
#	@echo "Downgrading database..."
#	. .venv/bin/activate && $(ALEMBIC_CMD) downgrade $(rev)
#
#his: ## 📋 Show the migration history
#	@echo "Alembic migration history:"
#	. .venv/bin/activate && $(ALEMBIC_CMD) history
#
#test: ## 🧪 Run tests
#	@echo "Starting pytesting..."
#	. .venv/bin/activate && pytest -v
#
#test_cov: ## 🧪 Run tests with coverage
#	@echo "Starting pytesting with coverage..."
#	. .venv/bin/activate && pytest -v --cov --cov-report=term-missing

