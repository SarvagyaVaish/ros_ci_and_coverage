from datetime import datetime


def get_time_str():
    now = datetime.now()
    s = now.strftime("%a, %b %d")
    return s
