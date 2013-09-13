#!/bin/bash

#jenkins bash script build

# resolve dependencies
pip install -r requirements/dev.txt
pip install -e .

# style report
flake8 --max-complexity 12 .

pep8 . > pep8_report.txt

#pylint --rcfile .pylintrc -f parseable *.py settings urls apps libs > pylint_report.txt || exit 0

# test
coverage run --branch --source=teracy `which django-admin.py` test --settings=teracy.html5boilerplate.test_settings

# coverage report
coverage xml --omit=*/__init__.py,teracy/html5boilerplate/test*
