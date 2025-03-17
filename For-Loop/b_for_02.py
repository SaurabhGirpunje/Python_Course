# Print all odd numbers from 1 to 50 using a for loop.

for i in range(1, 50, 2):
    print(i, end=" ")

print('\n')

for i in range(1, 51):
    if i % 2 != 0:
        print(i, end = " ")