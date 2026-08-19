num1 = [2,3,4,2,5,6]
num2 = [7,8,4,5,3]

result = num1+num2
print(result)

dup =[]
dup2 =[]

for i in result:
   if i not in dup:
      dup.append(i)
print(dup)

for i in result:
   if result.count(i)>1 and i not in dup2:
      dup2.append(i)
print(dup2)