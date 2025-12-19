class Animal:
    def __init__(self,name) -> None:
        self.name = name

    def make_sound(self):
        print('animal make some different sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('meow meow')  
    
class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('gheo gheo')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('beh beh beh')


don = Cat('real don')
don.make_sound

sheprad = Dog('Local Shephard')
sheprad.make_sound()

mess = Goat('L M')
mess.make_sound()

less = Goat('gora gori')

animals = [don,sheprad,mess,less]
for animal in animals:
    animal.make_sound()

   
