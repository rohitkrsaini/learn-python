add = lambda a,b: a+b
print(add(8,3))

# recurcive function

def fact(num):
    if(num == 1):
        return 1
    return num*fact(num-1)

print(fact(10))