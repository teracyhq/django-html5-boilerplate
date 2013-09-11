resolve:
	pip install -r requirements/dev.txt
	pip install -e .

check-style:
	flake8 .

test:
	coverage run --branch --source=teracy `which django-admin.py` test \
		--settings=teracy.html5boilerplate.test_settings teracy.html5boilerplate

report-coverage:
	coverage report --omit=*/__init__.py,teracy/html5boilerplate/test*

.DEFAULT_GOAL := resolve

.PHONY: resolve, check-style, test, report-coverage