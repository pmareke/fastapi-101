.DEFAULT_GOAL := help 

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: up
up: ## Run Streamlit app
		poetry run fastapi run main.py --reload

.PHONY: test
test: ## Run the tests
	 PYTHONPATH=. poetry run pytest tests -ra
