# number
x = 10
print(x,type(x))

#float
y = 3.14
print(y,type(y))

#string
y = 'rohit'
print(y,type(y))

# list
l = [10,20,"rohit",'w']
print(l,type(l))

#tuple
t = ("rohit", 15,'f')
print(t,type(t))

#dict

myDict ={
    "name":"Rohit",
    "age":"21"
}

print(myDict,type(myDict))

# boolean

status = True
print(status,type(status))

# set 
s ={10,20,30,30,40,50,60,60}
print(s,type(s))

# remove dublecate in list

num = [10,20,20,30,40,45,50,50,56]
print(list(set(num)))

tup = (10,15,15,20)
print(tuple(set(tup)))

s ="rohit"
print('m'in s)