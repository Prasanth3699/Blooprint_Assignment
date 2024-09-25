import logging
import time
from django.utils.deprecation import MiddlewareMixin

class APILoggingMiddleware(MiddlewareMixin):
    """
    Middleware to log API usage details.
    """

    def __init__(self, get_response=None):
        self.get_response = get_response
        self.logger = logging.getLogger('inventory')
        super().__init__(get_response)

    def process_request(self, request):
        # Record start time of request
        request.start_time = time.time()
        return None

    def process_response(self, request, response):
        # Calculate duration of request
        duration = time.time() - getattr(request, 'start_time', time.time())
        duration = round(duration * 1000, 2)  # Duration in milliseconds

        # Getting user information
        user = request.user.username if request.user.is_authenticated else 'Anonymous'

        # Log details
        log_message = (
            f"User: {user} | Method: {request.method} | "
            f"Path: {request.get_full_path()} | Status: {response.status_code} | "
            f"Duration: {duration}ms"
        )

        self.logger.info(log_message)

        return response
    
    # Logging the exception
    def process_exception(self, request, exception):
        self.logger.error(f"Exception occurred: {str(exception)}", exc_info=True)
        return None