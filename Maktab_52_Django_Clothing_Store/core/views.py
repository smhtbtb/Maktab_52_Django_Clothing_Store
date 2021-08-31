from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic


# These views were made just for some tests

class MyView(generic.TemplateView):
    template_name = 'base_temp/base.html'


def test(request):
    import logging
    logger = logging.getLogger('project')
    logger.debug('DEBUG MESSAGE')
    logger.info('INFO MESSAGE')
    logger.warning('WARNING MESSAGE')
    logger.error('ERROR MESSAGE (should be more than twenty characters)')
    logger.critical('CRITICAL MESSAGE')
    return HttpResponse('')
