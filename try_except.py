try:
    print(10/0)
# except:
#     print("you can do it")
except ArithmeticError as e:
    print(e)
