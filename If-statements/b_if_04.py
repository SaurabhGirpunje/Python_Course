# Check if a number is divisible by both 5 and 7.

num = int(input("Enter number: "))

if num % 5 == 0 and num % 7 == 0:
    print(f"{num} is divisible by 5 and 7")
else:
    print("Number not divisible by 5 and 7")