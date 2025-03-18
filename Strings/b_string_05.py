# Check if a string is a palindrome (e.g., "madam").

string1 = input("Enter the string : ")

revStr = string1[::-1]

if string1 == revStr:
    print("String is palindrome")
else:
    print("String is not palindrome")

# -------------------------------------------------------------------------------

# Using a Two-Pointer Approach

left, right = 0, len(string1) - 1
is_palindrome = True

while left < right:
    if string1[left] != string1[right]:
        is_palindrome = False
        break
    
    left += 1
    right -= 1

print("String is palindrome" if is_palindrome else "String is not palindrome")
