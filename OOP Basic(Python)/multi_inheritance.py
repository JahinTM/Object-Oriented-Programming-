class family:
    def __init__(self, address) -> None:
        self.address = address

class school:
    def __init__(self, id,level) -> None:
        self.id = id
        self.level = level
class sprots:
    def __init__(self,game) -> None:
        self.game = game

class student(family,school,sprots):
    def __init__(self, address,id,level,game) -> None:
        school.__init__(self,id,level)
        sprots.__init__(self,game)
        family.__init__(self,address)