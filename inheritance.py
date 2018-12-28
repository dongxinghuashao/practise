# inheritance 继承
# over write  重载

class Father:
    name = 'milesfashion'

    def eat(self):
        print("you can eat")


class Mother():
    def walk(self):
        print("you can walking")


class Son(Father, Mother):
    def eat(self):
        print("I can eat son")


smallMilefashion = Son()
smallMilefashion.eat()
smallMilefashion.walk()
