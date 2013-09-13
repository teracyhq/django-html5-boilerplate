teracy-django-html5-boilerplate
===============================

``teracy-django-html5-boilerplate`` is a Django wrapper application that includes `html5-boilerplate`_
assets and provides ``base.html`` for starting any web application with ``html5-boilerplate``.

The project mission is to port html5-boilerplate to Django development so that every Django project
could take and use it with ease, flexibility and customization by its needs.

Continuous Integration
----------------------

|travis build status|_

|jenkins build status|_



Usage
-----

1. Add "teracy.html5boilerplate" to your ``INSTALLED_APPS`` setting like this:
::

    INSTALLED_APPS += (
        'teracy.html5boilerplate',
    )

2. Extend the ``base.html`` like this:
::
    {% extends 'html5boilerplate/base.html' %}


Installation
------------

Add ``teracy-django-html5-boilerplate`` application into your requirements file:
::
    teracy-django-html5-boilerplate

Or with ``pip``:
::
    $ pip install teracy-django-html5-boilerplate

Or with ``setuptools``:

Download the source code at https://github.com/teracy-official/django-html5-boilerplate and:
::
    $ python setup.py install


Configuration
-------------

``teracy.html5boilerplate.context_processors.page`` context processor is provided to process
``page.author``, ``page.copyright`` and ``page.ga_id`` from django settings file like the
configuration below:
::
    TEMPLATE_CONTEXT_PROCESSORS += (
        'teracy.html5boilerplate.context_processors.page',
    )

    SITE_AUTHOR = 'Teracy'
    SITE_COPYRIGHT = 'Teracy, Inc'
    SITE_GA_ID = 'UA-42868657-2'

To include source code files instead of minified ones, add ``django.core.context_processors.debug``
to ``TEMPLATE_CONTEXT_PROCESSORS`` on **debug mode**.
::
    TEMPLATE_CONTEXT_PROCESSORS += (
        'django.core.context_processors.debug',
    )



Context Variables
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

Conventions:
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


Contributing
------------

1. File issues at https://issues.teracy.org/browse/DJHBP

2. Follow workflow at http://dev.teracy.org/docs/develop/workflow.html

3. Notices:

Make sure to resolve the dependency requirements:
::
    $ make resolve

Make sure to check the coding style:
::
    $ make check-style

Make sure to run tests:
::
    $ make test

Make sure to check the coverage report:
::
    $ make report-coverage


Authors and contributors
------------------------

- Hoat Le: http://github.com/hoatle


License
-------

BSD License
::
    Copyright (c) Teracy, Inc. and individual contributors.
    All rights reserved.

    Redistribution and use in source and binary forms, with or without modification,
    are permitted provided that the following conditions are met:

        1. Redistributions of source code must retain the above copyright notice,
           this list of conditions and the following disclaimer.

        2. Redistributions in binary form must reproduce the above copyright
           notice, this list of conditions and the following disclaimer in the
           documentation and/or other materials provided with the distribution.

        3. Neither the name of Teracy, Inc. nor the names of its contributors may be used
           to endorse or promote products derived from this software without
           specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
    ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
    ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

.. |travis build status| image:: https://travis-ci.org/teracy-official/django-html5-boilerplate.png?branch=develop
.. _travis build status: https://travis-ci.org/teracy-official/django-html5-boilerplate

.. |jenkins build status| image:: https://ci.teracy.org/buildStatus/icon?job=django-html5-boilerplate-develop
.. _jenkins build status: https://ci.teracy.org/job/django-html5-boilerplate-develop/

.. _html5-boilerplate: http://html5boilerplate.com
