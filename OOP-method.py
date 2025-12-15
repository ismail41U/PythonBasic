
class fruits:

    type = "Food Item"  # class variable

    def __init__(self, name, color, calorie):
        self.name = name
        self.color = color
        self.calorie = calorie

    # instance method
    def info(self):
        return f"Fruit Name: {self.name}, Color: {self.color}, Calories: {self.calorie}, Type: {fruits.type}"
    
    # instance method
    def is_healthy(self):
        return self.calorie < 100




fruit1 = fruits("Apple", "Red", 95)
fruit2 = fruits("Banana", "Yellow", 105)
fruit3 = fruits("Orange", "Orange", 62)

print(fruit1.info())
print(fruit2.info())
print(fruit3.info())
print(f"Is {fruit1.name} healthy ? : {'Yes' if fruit1.is_healthy() else 'No'}")
print(f"Is {fruit2.name} healthy ? : {'Yes' if fruit2.is_healthy() else 'No'}")
print(f"Is {fruit3.name} healthy ? : {'Yes' if fruit3.is_healthy() else 'No'}")

class Circle:
    pi = 3.14159  # class variable

    def __init__(self, radius=1): # default radius
        self.radius = radius

    # instance method
    def area(self):
        return Circle.pi * (self.radius ** 2)

    # instance method
    def circumference(self):
        return 2 * Circle.pi * self.radius

area1 = Circle(5).area()
area2 = Circle().area() # default radius
circumference1 = Circle(5).circumference()
circumference2 = Circle().circumference() # default radius
print(f"Area of circle with radius 5: {area1} / Circumference of circle with radius 5: {circumference1}")
print(f"Area of circle with default radius: {area2}, / Circumference of circle with radius : {circumference2}")