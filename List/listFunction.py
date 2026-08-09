l= [1,2,30]

#append
l.append(40)
print(l)

#insert
l.insert(2,25)
print(l)

#extend
l.extend([50,60,70,10,11,10,16,10])
print(l)

#remove
l.remove(70)
print(l)

#sort
l.sort()
print(l)

#count
print(l.count(10))

#frequancy count using set()
for i in set(l):
    print(i ,"=", l.count(i))
