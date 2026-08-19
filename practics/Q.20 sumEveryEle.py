list = [12,34,56,43,243,4564]
sumList = []

for num in list:
    total = 0

    while num>0:
        lastDigit = num%10
        total = total+lastDigit
        num = num//10
    sumList.append(total)
print(sumList)