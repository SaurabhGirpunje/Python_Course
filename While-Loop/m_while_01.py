# Find the factorial of a number using a while loop.

num = int(input("Enter number: "))
fact = 1

while num > 0:
    fact = fact * num
    num -= 1

print("Factorial of number is: ", fact)