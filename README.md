# Lagom dependency injection example

Example usage of https://github.com/meadsteve/lagom

## Running
```bash
pipenv install
pipenv run uvicorn entry:app --reload
```

## Testing
```bash
pipenv run pytest example
pipenv run mypy --ignore-missing-imports --strict-optional --check-untyped-defs .
```