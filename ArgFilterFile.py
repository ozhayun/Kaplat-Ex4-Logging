import logging
import RequestCounter


# This class add the request counter to every request
class ArgFilter(logging.Filter):
    def filter(self, record):
        record.arg = RequestCounter.get_req_count()
        return True
