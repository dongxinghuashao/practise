# object oriented

# class Student():
#     def eat(self):
#         print("milesfashion can eat")
#     def run(self):
#         print("milesfashion can run")
# miles=Student()
# miles.run()
#
# friut="apple"
# print(friut.upper())

# class Student:
#     def eat(self, name, age):
#         print(name + " can eat" + " and " + "age is " + age)
#
#
# Student().eat("milesfashion", "18")

class Student():
    name = "milesfahion"
    age = 20

    def eat(self):
        print(self.name, "can eat", " and age is", self.age)

    @staticmethod
    def run():
        print("you can run")

    def speak(self):
        print(self.name,"can speaking")



student1 = Student()
student1.run()
student2 = Student()
student2.eat()
student3=Student()
student3.speak()
