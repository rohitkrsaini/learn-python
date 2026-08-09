num = eval(input("enter the number "))

count = 0
for n in range(1,num):
    if(num%n==0):
        print(n)
        count+=n 
print("total = ",count)

if(count==num):
    print("it's is perfect number")
else:
    print("it's not a perfect number")