# coding:utf-8
from functools import wraps
from datetime import datetime


def func_cost(fn):
    @wraps(fn)
    def print_cost(*args, **kwargs):
        st = datetime.now()
        fn(*args, **kwargs)
        et = datetime.now()
        return et - st
    return print_cost