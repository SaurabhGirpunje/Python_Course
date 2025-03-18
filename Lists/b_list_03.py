# Write a program to find the largest number in a list.

values = [5, 12, 8, 20, 3, 15, 7, 25, 10, 18]

maxNum = 0

for i in values:
    if i > maxNum:
        maxNum = i

print("Largest number is : ", maxNum)