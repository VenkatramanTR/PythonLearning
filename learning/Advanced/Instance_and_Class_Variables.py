class Car:
    wheels = 4 # class variable (same for all the instances

    def __init__(self):
        self.name = 'BMW' #instance variable
        self.mil = '10' #instance variable (can be different for each instance)

car1 = Car()
car2 = Car()
car1.name = 'Benz'
car1.wheels = 5 #this will be changed for all the objects as this is a class variable
print(car1.name, car1.mil, car1.wheels)
print(car2.name, car2.mil, car1.wheels)