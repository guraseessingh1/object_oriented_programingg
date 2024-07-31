#creating blueprint(class)
#class consists of 2 things - propertys and functions

class Person():
    #propertys
    age=26
    height=180
    name=""
    #creating constructor function
    def __init__(self,age,height,name):
        print("constructor function called")
        self.age = age
        self.height = height
        self.name = name




#creating the object using the person class
sarbjit = Person(30,170,"sarbjit")
print(sarbjit.age)


#creating another object
gurasees = Person(13,155,"gurasees")
print(gurasees.height)
