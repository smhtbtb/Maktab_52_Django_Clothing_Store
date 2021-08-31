from django.utils import timezone
import logging


class TimingMiddleware:
    """
    A middleware that will help you to find the time between request and response
    """

    def __init__(self, get_response_func) -> None:
        self.get_response = get_response_func

    def __call__(self, request):
        time = timezone.now()
        response = self.get_response(request)
        timedelta = timezone.now() - time
        logger = logging.getLogger('timing')
        logger.info(f'The time between requests and responses: {timedelta} seconds')
        return response
