req_count = 0

def increase_req_count():
    global req_count
    req_count += 1

def get_req_count():
    return req_count