=====
html5boilerplate Django wrapper application
=====

vendor.html5boilerplate is a Django wrapper application that includes html5boilerplate assets
and provides base.html for starting any web application with html5boilerplate.
This base.html is flexible enough that you could override almost any block within it.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "vender.html5boilerplate" to your INSTALLED_APPS setting like this:

      INSTALLED_APPS = (

          'vendor.html5boilerplate',
      )

2. Extend the base.html like this:

      {% extends 'html5boilerplate/base.html' %}
