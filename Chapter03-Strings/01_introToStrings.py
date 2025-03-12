a ='hello' # Single quoted string
b = "hello" # Double quoted string
c = '''hello''' # Triple quoted string

print(a, b, c)

# Strings are immutable

name = "Hello"

name2 = name[:-1]
char1 = name[2]

print(name2)
print(char1)

print(name[-5:])
print(name[::-1])
print(name[::])
print(name[0:2])

name[2] = 'j'       # Strings are immutable and doesn't support assignment
print(name)