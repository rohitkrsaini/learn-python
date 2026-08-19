num = [1,2,3,5,6,7,9,10]
miss = []

for i in range(1,11):
   if i not in num:
    miss.append(i)

print(miss)