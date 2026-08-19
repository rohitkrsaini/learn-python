# 1 methods

str = "madam"
palindrom = str == str[::-1]

if (palindrom):
    print("it's palindrom number")
else:
    print("it's not a paindrom number")

# 2 methods

num = 42324

original = num
rev = 0

while num > 0:
    lastDigit = num % 10
    rev = rev * 10 + lastDigit
    num = num // 10

palNum = original == rev

if palNum:
    print("It's a palindrome number")
else:
    print("It's not a palindrome number")