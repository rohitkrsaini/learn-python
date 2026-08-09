total = 0
for a in range(1,6):
    total = total+a
print(total) 

name = "ROHIT"
for a in name:
    print(a,end=" ")
    print()

l =["Rohit",1,23]
for a in l:
    print(a)

# nested loop
for n in range(1,11):
    for c in range(1,11):
        print(n,"*",c," = ",n*c)
    print()

#break
for a in range(1,11):
    print(a)
    if a==5:
        break

#continous
for a in range(1,11):
    if a==6:
        continue
    print(a)