num = 25513
original = num
rev = 0

while(num>0):
    lastDigit = num%10
    rev = rev*10 +lastDigit
    num = num//10

print(f" origanal no is = { original }\n revrse no. is = { rev}")
