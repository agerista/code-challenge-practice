class Animal(object):

    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError()


class Cat(Animal):

    def talk(self):
        return 'meow'


class Dog(Animal):

    def talk(self):
        return 'woof'

garfield = Cat(name='Garfield')
odie = Dog(name='Odie')

print(garfield.name)  # 'Garfield'
print(garfield.talk())
print(odie.name)      # 'Odie'
print(odie.talk())


def test_cat_meows():
    garfield = Cat(name='Garfield')
    assert garfield.talk() == 'meow'


def test_create_animals():
    garfield = Cat(name='Garfield')
    odie = Dog(name='Odie')

    assert garfield.name == 'Garfield'
    assert odie.name == 'Odie'


def test_dog_barks():
    odie = Dog(name='Odie')
    assert odie.talk() == 'woof'

