# swap with third varivble
x=10
y=20
z=x
x=y
y=z
print("x = ",x,"y =",y)


#without third variable

a = 30
b= 50

print("a = ",a)
print("b = ", b)
a = a+b
b = a-b
a = a-b

print("a = ",a)
print("b = ", b)

r=5
s=15

r,s=s,r
print(r,s)