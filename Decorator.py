from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took { t2-t1 } time')
        return result
    return wrapper


@performance
def long_time():
    for i in range(10000000):
        i*5


long_time()


def my_decorator(func):
    def wrap():
        print("****")
        func()
        print("****")
    return wrap


@my_decorator
def hello():
    print("hello")


hello()
