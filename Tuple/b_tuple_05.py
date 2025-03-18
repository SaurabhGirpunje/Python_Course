# Count the occurrence of a specific element in a tuple.

tup1 = (1,2,3,7,4,10,8,10,2,4)

n1 = 4
count = 0

for i in tup1:
    if i == n1:
        count += 1

print(f"{n1} has occured {count} times")