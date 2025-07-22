.PHONY: install bdd clean setup

install:
	pip install behave black flake8

setup:
	mkdir -p test/reports

bdd:
	@echo "Ejecutando tests BDD desde test/features/..."
	behave test/features/ --format=pretty

bdd-verbose:
	behave test/features/ --format=pretty --verbose

bdd-junit:
	behave test/features/ --format=pretty --junit --junit-directory=test/reports

clean:
	rm -rf test/reports/ __pycache__/
	find . -name "*.pyc" -delete

ci: bdd
	@echo "Tests BDD completados"