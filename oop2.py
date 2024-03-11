class Car:
    def __init__(self, make, model, yom):
        self.make = make
        self.model = model 
        self.yom = yom


    def drive(self):
        return("toouirh!!")

    def run(self):
        return("rufhdbb!")

myCar = Car("Tesla", "truck", 2003)

class ElectricCar(Car):
    def __init__(self, make, model, yom):
        Car.__init__(self, make, model, yom)
        
    def charge(self):
        return(" I am charging my car")


    

print(myCar.yom)
print(myCar.drive())
print(ElectricCar.charge())

