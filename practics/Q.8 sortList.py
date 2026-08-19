num = [5,4,3,6,2,5]

for i in range(len(num)):
    for j in range(len(num)-1):
       if num[j]>num[j+1]:
           num[j],num[j+1] = num[j+1],num[j]

print(num)
s= str(num)
print(s[-5])