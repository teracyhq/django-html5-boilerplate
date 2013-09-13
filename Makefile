resolve:
	pip install -r requirements/dev.txt

check-style:
	flake8 --max-complexity 12 .
	pylint --rcfile .pylintrc *.py teracy

test:
	export DJANGO_SETTINGS_MODULE=teracy.html5boilerplate.test_settings
	coverage run --branch --source=teracy `which nosetests`

report-coverage:
	coverage report --omit=*/__init__.py,teracy/html5boilerplate/test*

.DEFAULT_GOAL := resolve

.PHONY: resolve, check-style, test, report-coverage
