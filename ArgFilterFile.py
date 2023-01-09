import logging
import RequestCounter


class ArgFilter(logging.Filter):
    def filter(self, record):
        # record.arg = 'request_counter'
        record.arg = RequestCounter.get_req_count()
        return True
