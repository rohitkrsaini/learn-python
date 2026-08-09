# write a function that task a list and return a evan number only

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def evanNum(num):
    evan = []

    for i in num :
     if(i%2==0):
        evan.append(i)
    return evan
    
print(evanNum(l))

#list comphesion

lis = [12,34,56,78,90,98,76,54,32,1,2,7,98]
evan = [n for n in lis if n%2==0]
print(evan)