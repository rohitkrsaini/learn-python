# prime number

num = eval(input("enter the number "))

count = 0

for n in range(1,(num+1)//2):
    if(num%n==0):
        count+=1

if(count == 1):
    print(num,"Given num is prime no.")
else:
    print(num,"Given num is not a prime no.")
