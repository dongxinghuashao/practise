# # define 下定义
# def Function_name():

# def func1():
#     print("milesfashion")
#
#
# func1()
# a = 10
# b = 10
# print(a + b)
# c = 20
# d = 20
# # print(c + d)
#
# def sum(num1, num2):
#     print(num1 + num2)
# sum(1, 2)
# sum(10, 10)
# sum(20, 20)
#
# def func2():
#     return ("hello milesfashion")
#
#
# def sum2(a, b):
#     return (a + b)
#
#
# a = sum2(1, 2)
# print(a)
# b = sum2(3, 3)
# print(b)
def converter(weight):
    ponds=weight/0.45
    print(ponds)
converter(300)

def converter2(weight=100):
    ponds=weight/0.45
    print(ponds)
converter2(weight=300)
converter2(400)
