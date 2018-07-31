class NameDescriptor:
    def __get__(self, instance, owner):
        #print(self)
        #print(instance)
        #print(owner)
        return instance._name

    def __set__(self, instance, value):
        #print(self)
        #print(instance)
        #print(value)
        instance._name = value

class Person:
    name = NameDescriptor()

    def __init__(self, name):
        self._name = name

if __name__ == '__main__':
    bob = Person('Bob')
    print(bob.__dict__)

    print(bob.name)
    bob.name = 'William'
    print(bob.name)
