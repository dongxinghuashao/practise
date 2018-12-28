# file = open("milesfashion.txt")
# text = file.read()
# print(text)
# file.close()

# with open('milesfashion.txt') as file:
#     print(file.read())
with open('milesfashion.txt','a') as f:
    f.write('milesfashion\n')

print(help(open))