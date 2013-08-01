"""
A set of request context processors provied by teracy.html5boilerplate.
"""
#from django.conf import settings


def page(request):
    """
    page context processor which adds default context to 'page' via settings module.

    settings.site.author => page.author
    settings.site.copyright => page.copyright
    settings.site.ga_id => page.ga_id
    """

    context_extras = {}

    page = {}

    #TODO set values here

    context_extras['page'] = page

    return context_extras
