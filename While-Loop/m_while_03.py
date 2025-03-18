# Count the number of digits in a given number using a while loop.

num = int(input("Enter number"))
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Count of number is : ", count)