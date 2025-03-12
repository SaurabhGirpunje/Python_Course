# TYPE() FUNCTION AND TYPECASTING

a = 32
print(type(a))

a = "Hello"
print(type(a))

a = 32.9
print(type(a))

a = True
print(type(a))

a = None
print(type(a))

print("-------------------------------------------")

a = 32
b = float(a)
print(type(b))


a = 567
b = str(a)
print(type(b))

a = 0
b = bool(a)
print(type(b))

a = -8
b = bool(a)
print("Value of b : ", b, "and type is ", type(b))

a = 0
b = None(a)
print(type(b))