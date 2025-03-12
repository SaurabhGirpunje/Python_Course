a = "hello World"

print(len(a))

print(a.endswith("rl"))
print(a.endswith("rld"))

print(a.startswith("h"))
print(a.startswith("H"))

# print(a.capitalize())
# print(a.title())
# print(a.swapcase())

s = "Hello World"

print(s.upper())    # 'HELLO WORLD' - Convert to uppercase
print(s.lower())    # 'hello world' - Convert to lowercase
print(s.title())    # 'Hello World' - Convert first letter of each word to uppercase
print(s.capitalize())  # 'Hello world' - First letter uppercase, rest lowercase
print(s.swapcase()) # 'hELLO wORLD' - Swap uppercase/lowercase
print("Is space: ", s.isspace())

s = "   "
print("Is space: ", s.isspace())


s = "hello123"

print(s.isalpha())  # False - Checks if all characters are alphabets
print(s.isdigit())  # False - Checks if all characters are digits
print(s.isalnum())  # True - Checks if all characters are alphanumeric (A-Z, 0-9)
print(s.isspace())  # False - Checks if string contains only spaces
print(s.islower())  # True - Checks if all characters are lowercase
print(s.isupper())  # False - Checks if all characters are uppercase


s = "hello world"

print(s.find("world"))  # 6 - Returns first index of substring (-1 if not found)
print(s.index("world")) # 6 - Like `find()` but raises error if not found
print(s.replace("world", "Python"))  # 'hello Python' - Replace substring
print(s.count("o"))     # 2 - Counts occurrences of substring

s = "apple,banana,cherry"

print(s.split(","))  # ['apple', 'banana', 'cherry'] - Split into list
print("-".join(["a", "b", "c"]))  # 'a-b-c' - Join list with separator

lst = ['gmail', 'com']
print("sam", "@".join(lst))

# lst = [1,2,3]                 # gives error as it requires string instance
# print("sam", "@".join(lst))


s = "   hello world   "

print(s.strip())  # 'hello world' - Removes leading & trailing spaces
print(s.lstrip()) # 'hello world   ' - Removes leading spaces
print(s.rstrip()) # '   hello world' - Removes trailing spaces


name = "Alice"
age = 25

print(f"My name is {name} and I am {age} years old.")  # f-string formatting
print("My name is {} and I am {} years old.".format(name, age))  # Using format()


s = "hello"

encoded = s.encode()  # Convert to bytes
print(encoded)  # b'hello'

decoded = encoded.decode()  # Convert back to string
print(decoded)  # 'hello'
