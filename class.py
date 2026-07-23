class book:
    def display(self):
        print("The author is afrid")
s1 = book()
s1.display()


class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print("name :",self.name)
        print("age :",self.age)
s1 = student("ofiq",20)
s1.show()


class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def show(self):
        print("brand name :",self.brand)
        print("colour :",self.color)
s1 = car("fortuner","black")
s1.show()