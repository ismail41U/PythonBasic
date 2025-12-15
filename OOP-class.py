
# class
class Person:
    # class attributes
    address = "Unknown" # static (rarely changes)

    # constructor
    def __init__(self, name, age): 
        # object attributes
        self.name = name  # instance variable
        self.age = age    # instance variable
        
        # method
    def information(self):
        return f"Person1 Name :{self.name} Person1 Year :{self.age} Address :{Person.address}"
    

    # object (instance) creation
person1 = Person(name ="Alice", age = 30)
person2 = Person(name ="Bob", age = 25)

# updating class attribute
Person.address = "123 Main St"
person1.name = "Alice Smith"

 # accessing class attributes and methods
print(f"Person1 Name :{person1.name} /Person1 Year :{person1.age}/ Address :{Person.address}")
print(f"Person2 Name :{person2.name} /Person2 Year :{person2.age}/ Address :{Person.address}")

