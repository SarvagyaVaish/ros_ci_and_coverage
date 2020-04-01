from datetime import datetime


def get_time_str():
    now = datetime.now()
    s = now.strftime("%a, %b %d")
    return s


def foo_bar():
    if 4 % 2 == 0:
        return True
    else:
        return False


def foo_bar_2():
    if 4 % 2 == 0:
        return True
    else:
        return False


def foo_bar_3():
    if 4 % 2 == 0:
        return True
    else:
        return False
