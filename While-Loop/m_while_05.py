# Reverse a string using a while loop.

st = input("Enter the string: ")    #String
count = len(st)
revSt = ""

while count > 0:
    revSt = revSt + st[count - 1]
    count -= 1

print(revSt)
