# class Students:
#     name="milesfashion"
#     age=20
#     def run(self):
#         print(self.name,"can runnnig")
#         print(self.name,"is",self.age)
# s1=Students()
# s1.run()
class Students():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(self.name, "can running")
        print(self.name, "is", self.age)


s1 = Students(name='milesfahion',age= '20')
s2 = Students("james", "18")
s1.run()
s2.run()
