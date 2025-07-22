.PHONY: install bdd clean

install:
	pip install -r requirements-dev.txt

bdd:
	behave features/

clean:
	rm -rf reports/ __pycache__/

ci: bdd