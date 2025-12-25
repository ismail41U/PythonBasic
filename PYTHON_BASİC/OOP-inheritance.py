  # inheritance example
class Animal:
    callout ="Animal Sound"

    def __init__(self,name,breed,weight):
        self.breed = breed
        self.name = name
        self.weight = weight
    
    def callOut(self):
        self.sound = "Roar !!!"
        return self.sound
    
class Dog(Animal):
    def __init__(self,name,breed,weight,age):
        Animal.__init__(self,name,breed,weight)
        self.age = age

        # overriding callOut method
    def callOut(self):
        self.sound = "woof woof !!!"
        return self.sound
    
    def sayHi(self):
        print("Hi, I am a Dog")

class Cat(Animal):
    def __init__(self,name,breed,weight,color):
        Animal.__init__(self,name,breed,weight) # using(self) super() to call parent constructor
        self.color = color

    def callOut(self):
        self.sound = "Meow Meow !!!"
        return self.sound
    
    def sayHi(self):
        print("Hi, I am a Cat")



a1 = Animal("Lion","Leo",190)
dog1 = Dog("Bulldog","Alex", 30 ,5)
cat1 = Cat("Persian","Luna", 8 ,"White")
dog1.sayHi()
cat1.sayHi()

print(f"Animal Breed: {a1.breed}, Name: {a1.name}, Weight: {a1.weight}kg, Sound: {a1.callOut()}")
print(f"Dog Breed: {dog1.breed}, Name: {dog1.name}, Weight: {dog1.weight}kg, Sound: {dog1.callOut()}, Age: {dog1.age} years")
print(f"Cat Breed: {cat1.breed}, Name: {cat1.name}, Weight: {cat1.weight}kg, ,Sound: {cat1.callOut()}, Color: {cat1.color}")