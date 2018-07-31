import time

def trace(fname):
    def file_trace(func):
        def call_func(*args, **kwargs):
            with open(fname, 'a+') as fd:
                fd.write('{}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
                fd.write('Calling {}: {}, {}\n'.format(func.__name__, args, kwargs))
                r = func(*args, **kwargs)
                fd.write('{} returns {}\n'.format(func.__name__, r))
                fd.flush()
                return r
        return call_func
    return file_trace

@trace('debug3.log')
def square(x):
    return x*x

@trace('debug3.log')
def quadratic(x, a, b, c):
    return a*x*x + b*x + c

square(10)
time.sleep(2)
quadratic(15, a=2, b=3, c=1)
