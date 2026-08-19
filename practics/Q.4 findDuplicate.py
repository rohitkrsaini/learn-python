list = [1,2,3,4,5,3,6,7,5,8,9,1]
dup = []

for i in list:
    if list.count(i)>1 and i not in dup:
        dup.append(i)

print(f"duplicate elemant = {dup}")
