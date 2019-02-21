import time
import functools

class lazy_property:
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, cls):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val

def lazy_property1(fn):
    attr = '_lazy__' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr):
            setattr(self, attr, fn(self))
        return getattr(self, attr)
   
    return _lazy_property


class Person:
    def __init__(self):
        self.count = 0   

    @lazy_property
    def one(self):
        time.sleep(2)
        self.count += 1
        return 'one'

    @lazy_property
    def two(self):
        time.sleep(2)
        self.count += 1
        return 'two'

if __name__ == '__main__':
    p = Person()
    print('p.one[0]:{}'.format(p.one))
    print('p.one[1]:{}'.format(p.one))
    print(p.count)

    print('p.two[0]:{}'.format(p.two))
    print('p.two[1]:{}'.format(p.two))
    print(p.count)
