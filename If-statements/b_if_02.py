# Check if a number is even or odd using an if statement.

num = int(input("Enter number: "))

if num % 2 == 0 and num != 0:
    print("Number is even")
elif num % 2 != 0 and num != 0:
    print("Number is odd")
else:
    print("Entered number is zero, enter another number")