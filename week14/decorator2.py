import time
def time_decorator(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('Process time: {}'.format(end - start))
    return inner

def say_name(name):
    time.sleep(2)
    print(name)

greet = time_decorator(say_name)
greet('Fabricio')