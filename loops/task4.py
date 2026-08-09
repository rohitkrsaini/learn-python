# reverse number 

num = eval(input("enter the number ")) 
number = num

reverse = 0
count = 0

while(num>0):
    n = num%10
    reverse = reverse*10 + n
    num = num//10
    count+=1

print(number," your number")
print(reverse,"reverse number")
print("total digit = ", count)