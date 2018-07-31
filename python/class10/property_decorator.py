##class Person:
##    def __init__(self, name):
##        self._name = name
##
##    def get_name(self):
##        print('fetch...')
##        return self._name
##
##    def set_name(self, value):
##        print('changing...')
##        self._name = value
##
##    name = property(fget=get_name, fset=set_name)

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):
        print('changing...')
        self._name = value

john = Person('John')
print(john.name)
john.name = 'Jack'
print(john.name)
