class Book:
    def __init__(self,name) -> None:
        self.name = name

    def read(self):
        raise NotImplementedError
    
class Physics(Book):
    def __init__(self, name,lab) -> None:
        self.lab=lab
        super().__init__(name)
    def read(self):
        print('reading physics vector chapter')

topor = Physics('topon',True)
print(issubclass(Physics,Book))
print(isinstance(topor,Physics))
print(isinstance(topor,Book))

topor.read()