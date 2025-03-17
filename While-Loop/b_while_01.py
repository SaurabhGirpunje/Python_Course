# Write a program to print numbers from 1 to 10 using a while loop.

num = 1

while num <= 10:
    print(num)
    num += 1

# -----------------------------------------------------------------------------

# Using Recursion:
# Here, n=1 is a default argument. It only takes effect when no argument is provided during the function call.

def print_numbers(n=1):
    if n > 10:
        return
    print(n)
    print_numbers(n+1)

print_numbers()