clean:
	rm -rf dist/ 
	rm -rf build/ 
	rm -rf **/__pycache__ 
	rm -rf .pytest_cache 
	rm -rf examplecli.egg-info
	rm -rf example_cli.egg-info
	rm -rf .coverage 
	rm -rf coverage.xml 
	rm -rf **/*.pyc
	rm -rf htmlcov

test:
	python -m unittest
	
lint:
	pylint examplecli
	pylint -d missing-class-docstring tests

coverage:
	coverage run
	coverage report
	coverage xml

local-build:
	pip install wheel
	scripts/local-build.sh
