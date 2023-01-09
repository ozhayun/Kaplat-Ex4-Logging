req_count = 0


# This function increase request count global variable with 1
def increase_req_count():
    global req_count
    req_count += 1


# This function return the request count for logs use
def get_req_count():
    return req_count
