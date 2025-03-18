# Remove duplicates from a list.

values = [5, 12, 8, 20, 3, 15, 7, 25, 10, 18, 7, 20, 5]

set1 = set(values)

print(set1)

# ----------------------------------------------------------------------

uniqueEle = []

for i in values:
    if i not in uniqueEle:
        uniqueEle.append(i)

print(uniqueEle)

