# Count the number of vowels in a string.

string = input("Enter the string: ").lower()

vowels = "aeiou"
count = 0

for i in string:
    if i in vowels:
        count += 1

print(f"Number of vowels in {string} is {count}")