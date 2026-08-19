num = int(input("enter the num "))

sum = 0

for i in range(1,num//2+1):
    if num%2==0:
        sum+=i

if sum == num:
    print("it's is perfact number")
else:
    print("it's not perfact number")