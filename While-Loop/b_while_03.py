# Find the sum of digits of a number using a while loop.

num = int(input("Enter Number: "))

sumDigit = 0

while num != 0:                 # while num is also equivalent to num != 0
    sumDigit += num % 10
    num = num // 10

print(sumDigit)