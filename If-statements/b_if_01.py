# Write a program to check if a number is positive, negative, or zero.

num = int(input("Enter number: "))

if num < 0:
    print("Number is negative")
elif num > 0:
    print("Number is positive")
else:
    print("Number is zero")