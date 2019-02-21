class Pet(object):
    def __init__(self, animal=None):
        self.pet = animal
    
    def show(self):
        pet = self.pet()
        print('a {}'.format(pet))
        print('{}'.format(pet.speak()))


class Cat:
    def speak(self):
        return 'meow'

    def __str__(self):
        return 'cat'


class Dog:
    def speak(self):
        return 'woof'

    def __str__(self):
        return 'dog'


if __name__ == '__main__':
     cat = Pet(Cat)
     cat.show()
     dog = Pet(Dog)
     dog.show()

     
