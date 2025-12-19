class Leptop:
    def __init__(self, brand, color, memory, price):
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Running Laptop: {self.brand}'

    def coding(self):
        return f'Learning Python and practicing'

class Phone:
    def __init__(self, brand, price, color, memory):
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Phone is running'

    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with text: {text}'

class Camera:
    def __init__(self, brand, price, color, pixel):
        self.brand = brand
        self.price = price
        self.color = color
        self.pixel = pixel

    def run(self):
        pass

    def change_lens(self):
        pass

# Function to get user input for laptop details
def get_laptop_details():
    brand = input("Enter laptop brand: ")
    color = input("Enter laptop color: ")
    memory = input("Enter laptop memory: ")
    price = float(input("Enter laptop price: "))
    return Leptop(brand, color, memory, price)

# Function to get user input for phone details
def get_phone_details():
    brand = input("Enter phone brand: ")
    color = input("Enter phone color: ")
    memory = input("Enter phone memory: ")
    price = float(input("Enter phone price: "))
    return Phone(brand, price, color, memory)

# Function to get user input for camera details
def get_camera_details():
    brand = input("Enter camera brand: ")
    color = input("Enter camera color: ")
    pixel = input("Enter camera pixel: ")
    price = float(input("Enter camera price: "))
    return Camera(brand, price, color, pixel)

# Take user input to choose which device details they want to enter
print("Options:")
print("1. Enter laptop details")
print("2. Enter phone details")
print("3. Enter camera details")
option = int(input("Enter your choice (1/2/3): "))

# Based on the user's choice, get the respective details
if option == 1:
    laptop = get_laptop_details()
    print("Laptop details:")
    print("Brand:", laptop.brand)
    print("Color:", laptop.color)
    print("Memory:", laptop.memory)
    print("Price:", laptop.price)
elif option == 2:
    phone = get_phone_details()
    print("Phone details:")
    print("Brand:", phone.brand)
    print("Color:", phone.color)
    print("Memory:", phone.memory)
    print("Price:", phone.price)
elif option == 3:
    camera = get_camera_details()
    print("Camera details:")
    print("Brand:", camera.brand)
    print("Color:", camera.color)
    print("Pixel:", camera.pixel)
    print("Price:", camera.price)
else:
    print("Invalid option selected")
