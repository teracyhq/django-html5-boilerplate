"""
urls configuration, this should be configured and included as root url like:

urlpatterns += (
    url(r'', include('teracy.html5boilerplate.urls')),
)

credit goes to https://github.com/mattsnider/django-html5-boilerplate/blob/master/dh5bp/urls.py
"""

from django.conf import settings
from django.conf.urls import patterns, url
from django.views.generic import RedirectView, TemplateView


urlpatterns = patterns(
    '',
    url(r'^crossdomain\.xml$', TemplateView.as_view(
        template_name='html5boilerplate/crossdomain.xml'),
        name='html5boilerplate'),
    url('^humans\.txt$', TemplateView.as_view(
        template_name='html5boilerplate/humans.txt'),
        name='html5boilerplate'),
    url('^robots\.txt$', TemplateView.as_view(
        template_name='html5boilerplate/robots.txt'),
        name='html5boilerplate'),
    url('^apple-touch-icon-precomposed\.png$', RedirectView.as_view(
        url='%shtml5boilerplate/apple-touch-icon-precomposed.png' % settings.STATIC_URL),
        name='html5boilerplate'),
)
