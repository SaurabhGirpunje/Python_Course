# Use a while loop to print even numbers from 2 to 20.

num = 1

while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1

# -------------------------------------------------------------------

# Using Recursion

def evenNo(num=2):
    if num > 20:
        return
    print(num)
    evenNo(num+2)

evenNo()