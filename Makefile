# Thanks to http://stackoverflow.com/questions/2214575/passing-arguments-to-make-run
# If the first argument is "test"...
ifeq (test,$(firstword $(MAKECMDGOALS)))
    # use the rest as arguments for "test"
    TEST_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
    # ...and turn them into do-nothing targets
    $(eval $(TEST_ARGS):;@:)
endif

resolve:
	pip install -r requirements/dev.txt
	pip install -e .

check-style:
	flake8 .

test:
	coverage run --branch --source=teracy `which django-admin.py` test \
		--settings=teracy.html5boilerplate.test_settings $(TEST_ARGS)

report-coverage:
	coverage report --omit=*/__init__.py,teracy/html5boilerplate/test*

.DEFAULT_GOAL := resolve

.PHONY: resolve, check-style, test, report-coverage