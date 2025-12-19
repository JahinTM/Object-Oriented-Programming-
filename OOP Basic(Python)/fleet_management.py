class Company:
    def __init__(self, name, address):
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counters = []
        self.managers = []
        self.supervisors = []
        self.fares = []

class Driver:
    def __init__(self, name, license, age):
        self.name = name
        self.license = license
        self.age = age

class Counter:
    def __init__(self):
        pass
    
    def purchase_ticket(self, start, destination):
        pass

class Passenger:
    pass

class Supervisor:
    pass

class manager:
    pass

lal_mia = Driver('a', '123', 32)
