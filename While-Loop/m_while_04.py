# Find the sum of even and odd digits separately from a number.

num = int(input("Enter the number: "))

even, odd = 0, 0

while num > 0:
    rem = num % 10
    num = num // 10
    
    if rem % 2 == 0:
        even += rem
    else:
        odd += rem

print("Even: ", even, " ", "Odd: ", odd)