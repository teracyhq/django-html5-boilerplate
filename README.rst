django-html5-boilerplate |build status|_
========================================

django-html5-boilerplate is a Django wrapper application that includes html5-boilerplate assets
and provides base.html for starting any web application with html5-boilerplate.
This base.html is flexible enough that you could override almost any block within it.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add dependency
::
    No dependency.

2. Add "teracy.html5boilerplate" to your INSTALLED_APPS setting like this:
::

    INSTALLED_APPS += (
        'teracy.html5boilerplate',
    )

3. Extend the base.html like this:
::
    {% extends 'html5boilerplate/base.html' %}

Context variables
-----------------

Context variables are expected to be included in a dictionary variable named: "page".
::
    page.lang            - "lang" attribute for <html> tag. Default: "en".
    page.dir             - "dir" attribute for <html> tag. Default: "ltr".
    page.charset         - meta charset value. Default: "utf-8".
    page.x_ua_compatible - "content" for http-equiv="X-UA-Compatible" meta tag. Default: "IE=edge,chrome=1".
    page.description     - "content" for "description" name meta tag. Default: None.
    page.keywords        - "content" for "keywords" name meta tag. Default: None.
    page.author          - "content" for "author" name meta tag. Default: None.
    page.copyright       - "content" for "copyright" name meta tag. Default: None.
    page.title           - value for <title> tag. Default: None.
    page.ga_id           - id for google analytics. Default: None.

Blocks
------

Convention notice:
::
    [block_name]
        [child_block_name]

The page structure is defined as following:
::
    <html>
        <head>
            [meta]
            [meta_extra]
            [title]
            [apple_touch_icon]
            [favicon]
            [stylesheet]
            [javascript]
        </head>
        <body class=[body_class]>
            [browser_outdated]
            [body_content]
            [body_extra]
                [jquery_loader]
                [google_analytics]
        </body>
    </html>

By default:

* [meta]: includes basic meta data of a page.

* [meta_extra]: should be used to provide more meta data for the page (for example: open graph,
twitter cards, apple app id, etc.).

* [title]: should provide page.title context to set the page's title.

* [apple_touch_icon]: Place apple-touch-icon.png in the root directory or set it explict here on this block.

* [favicon]: Place favicon.ico in the root directory or set it explicit here on this block.

* [stylesheet]: Load 'html5boilerplate/css/normalize.css' and 'html5boilerplate/css/main.css' by default.

* [javascript]: Load 'html5boilerplate/js/vendor/modernizr-2.6.2.min.js' by default.

* [body_class]: Set class to <body> tag.

* [browser_outdated]: Outdated message to be displayed when IE6 and below are used to access the page.

* [body_content]: The main content block.

* [body_extra]: Includes 2 children blocks: [jquery_loader] and [google_analytics].

* [jquery_loader]: Load jquery.

* [google_analytics]: Setup google analytics code if "page.ga_id" context is provided.


How to develop and contribute
-----------------------------

1. Make sure to resolve the dependency requirements:
::
    $ make resolve

2. Make sure to check the coding style:
::
    $ make check-style

3. Make sure to run tests:
::
    $ make test

4. Make sure to check the coverage report:
::
    $ make report-coverage

.. |build status| image:: https://travis-ci.org/teracy-official/django-html5-boilerplate.png?branch=develop
.. _build status: https://travis-ci.org/teracy-official/django-html5-boilerplate
