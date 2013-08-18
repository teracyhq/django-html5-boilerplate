from __future__ import absolute_import
from django.conf import settings
from django.test import SimpleTestCase
from django.test.client import RequestFactory
from teracy.html5boilerplate.context_processors import page


class ContextProcessorsTest(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def tearDown(self):
        settings.SITE_AUTHOR = None
        settings.SITE_COPYRIGHT = None
        settings.SITE_GA_ID = None

    def test_module_api(self):
        """
        Tests module's defined APIs
        """
        self.assertIsNotNone(page,
                             'teracy.html5boilerplate.context_processors.page must be available')

    def test_empty_settings(self):
        """
        Tests that there is no settings, all default settings for
        SITE_AUTHOR
        SITE_COPYRIGHT
        SITE_GA_ID
        """
        request = self.factory.get('/')
        context_extras = page(request)
        self.assertIsInstance(context_extras, dict, 'context_extras must be a dict')

        page_context = context_extras['page']
        self.assertEqual(page_context, {}, 'page_context must be empty dict')

    def test_site_author(self):
        """
        Tests that only SITE_AUTHOR is defined
        """
        settings.SITE_AUTHOR = 'Teracy'
        request = self.factory.get('/')
        context_extras = page(request)
        page_context = context_extras['page']
        expected_page_context = {
            'author': settings.SITE_AUTHOR
        }
        self.assertEqual(page_context, expected_page_context,
                         "%s must be %s" % (page_context, expected_page_context))

    def test_site_copyright(self):
        """
        Tests that only SITE_COPYRIGHT is defined
        """
        settings.SITE_COPYRIGHT = 'Teracy, Inc'
        request = self.factory.get('/')
        context_extras = page(request)
        page_context = context_extras['page']
        expected_page_context = {
            'copyright': settings.SITE_COPYRIGHT
        }
        self.assertEqual(page_context, expected_page_context,
                         '%s must be %s' % (page_context, expected_page_context))

    def test_ga_id(self):
        """
        Tests that only SITE_GA_ID is defined
        """
        settings.SITE_GA_ID = 'UA-42868657-2'
        request = self.factory.get('/')
        context_extras = page(request)
        page_context = context_extras['page']
        expected_page_context = {
            'ga_id': settings.SITE_GA_ID
        }
        self.assertEqual(page_context, expected_page_context,
                         '%s must be %s' % (page_context, expected_page_context))

    def test_all(self):
        """
        Tests when all available settings are defined
        """
        settings.SITE_AUTHOR = 'Teracy'
        settings.SITE_COPYRIGHT = 'Teracy, Inc'
        settings.SITE_GA_ID = 'UA-42868657-2'

        request = self.factory.get('/')
        context_extras = page(request)
        page_context = context_extras['page']
        self.assertEqual(page_context.author, settings.SITE_AUTHOR,
                         '%s must be %s' % (page_context.author, settings.SITE_AUTHOR))
        self.assertEqual(page_context.copyright, settings.SITE_COPYRIGHT,
                         '%s must be %s' % (page_context.copyright, settings.SITE_COPYRIGHT))
        self.assertEqual(page_context.ga_id, settings.SITE_GA_ID,
                         '%s must be %s' % (page_context.ga_id, settings.SITE_GA_ID))

    def test_complex(self):
        """
        Tests when random settings are defined, complex cases
        """
        settings.SITE_AUTHOR = 'Teracy'
        settings.SITE_COPYRIGHT = 'Teracy, Inc'
        request = self.factory.get('/')
        context_extras = page(request)
        page_context = context_extras.page

        self.assertEqual(page_context.author, settings.SITE_AUTHOR,
                         '%s must be %s' % (page_context.author, settings.SITE_AUTHOR))
        self.assertEqual(page_context.copyright, settings.SITE_COPYRIGHT,
                         '%s must be %s' % (page_context.copyright, settings.SITE_COPYRIGHT))
