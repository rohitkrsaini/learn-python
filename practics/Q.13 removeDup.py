num =[ 1,2,3,2,4,5,3,6,7,8,4,8,7]
dup =[]

for i in num:
    if i not in dup:
        dup.append(i)

print(dup)