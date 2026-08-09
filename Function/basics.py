def hello():
    print("hello Rohit")
hello()

# parameter function
def add(a,b):
    return a+b

addVal = add(3,2)
print(addVal)

def seq(num1,):
    return num1*num1

seqVal = seq(int(input("enter the num ")))
if(seqVal>=20):
    print("seq is : ",seqVal)
    print("grater then 20")
else:
    print("seq is : ",seqVal)
    print("less then 20")

# global variable
x = 4
def printGlobalVari():
    global x
    x = 6
    print(x)
def printGlobalVariable():
    print(x)
printGlobalVari()
printGlobalVariable()

