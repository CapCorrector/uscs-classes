class Inspector:
    def inspect(self):
        return '{}: {}'.format(self.__class__.__name__, self._gather_attrs())
    def _gather_attrs(self):
        attrs = ['{}={}'.format(key, getattr(self, key)) for key in sorted(self.__dict__)]
        return ', '.join(attrs)

class Foo(Inspector):
    count = 0
    def __init__(self):
        self.attr10 = Foo.count
        self.attr23 = Foo.count + 1

class Bar(Foo):
    pass

class Baz:
    pass

class Qux(Bar, Baz):
    pass

class Xyz(Baz, Inspector):
    def __init__(self):
        self.greet = 'Hello'

if __name__ == '__main__':
    f = Foo()
    print(f.__class__.__name__)
    print(f.__class__.__bases__)
    b = Bar()
    print(b.__class__.__name__)
    print(b.__class__.__bases__)
    q = Qux()
    print(q.__class__.__name__)
    print(q.__class__.__bases__)

    print(f.inspect())

    x = Xyz()
    print(x.inspect())
