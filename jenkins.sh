#!/bin/bash

#jenkins bash script build

# resolve dependencies
pip install -r requirements/dev.txt

# style report
flake8 --max-complexity 12 .

pep8 . > pep8_report.txt

# test
export DJANGO_SETTINGS_MODULE=teracy.html5boilerplate.test_settings

coverage run --branch --source=teracy `which nosetests` --with-xunit

# coverage report
coverage xml --omit=*/__init__.py,teracy/html5boilerplate/test*

# must be the last command to exit 0, otherwise, the next command will not be executed.
pylint --rcfile .pylintrc -f parseable *.py teracy > pylint_report.txt || exit 0
