# Write a while loop to reverse a given number (e.g., 123 → 321).

num = int(input("Enter number: "))
revNum = 0

while num:
    revNum = revNum * 10 + num % 10
    num //= 10
    
print(revNum)

