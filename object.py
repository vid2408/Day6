class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# create a new object of Person class
harry = Person()

print(Person.greet)

print(harry.greet)

harry.greet()