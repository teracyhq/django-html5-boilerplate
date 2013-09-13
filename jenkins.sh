#!/bin/bash

#jenkins bash script build

# resolve dependencies
pip install -r requirements/dev.txt

# style report
flake8 --max-complexity 12 .

pep8 . > pep8_report.txt

pylint --rcfile .pylintrc -f parseable *.py teracy > pylint_report.txt || exit 0

# test
export DJANGO_SETTINGS_MODULE=teracy.html5boilerplate.test_settings
coverage run --branch --source=teracy `which nosetests` --with-xunit --xunit-file=nosetests.xml

# coverage report
coverage xml --omit=*/__init__.py,teracy/html5boilerplate/test*
