class Person:
    def __init__(self, age, height, name):
        self.age = age
        self.height = height
        self.name = name


    def eat(self):
        return "I love food"

    def drive(self):
        return "I drive a Voxy"
myPerson = Person(29, 169, "Jack Doe")

print(myPerson.age)
print(myPerson.eat())
print(myPerson.drive())




