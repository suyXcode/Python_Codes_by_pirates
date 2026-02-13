class Demo:
    a = 10
    b = 20


ob1 = Demo()
ob2 = Demo()

# Accessing propeerties by using class
print(Demo.a)
print(Demo.b)
print('='*15)
# Accessing propeerties by using object
print(ob1.a)
print(ob1.b)
print('='*15)
print(ob2.a)
print(ob2.b)

print('='*15)
# Modifying the properties
ob2.a = True
print(Demo.a)
print(ob1.a)
print(ob2.a)
