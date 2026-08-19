str = "namaste devloper"
fre = {}

for i in str:
    if i != ' ':
        if i in fre:
            fre[i]+=1
        else:
            fre[i]=1

for key,value in fre.items():
    print(key,":",value)
