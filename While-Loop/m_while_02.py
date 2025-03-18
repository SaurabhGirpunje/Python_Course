# Print the Fibonacci sequence up to n terms using a while loop.
# 0,1,1,2,3,5,8,13,21,34,55,....

num = int(input("Enter number: "))

list1 = [0,1]
sum = 0

while len(list1) < num:
    sum = list1[-2] + list1[-1]
    list1.append(sum)

print(list1)