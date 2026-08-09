w = "welcome"
# print(len(w))

for a in range(len(w)):
    print(a,w[a])

#lowercase
x = " i am Rohit  "
l = x.lower()
print(l)

#upper case
u = x.upper()
print(u)

#strip
s =x.strip()
print(s)

#replese
print(x.replace("Rohit","ROHIT"))

#split
print(x.split(" "))

#alpha
q= "rohit12"
print(q.isalpha())

#string variable

age=24
print(f"my age is {age}")

#format
name ="rohit"
print("my name is {1}. and age is {0}".format(name,age))