text = "namaste developer"

count = 0

for i in text:
    if i in "aeiou":
        count += 1

print("Vowels:", count)