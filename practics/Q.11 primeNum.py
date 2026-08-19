num = int(input("given number "))

prime = True

for i in range(2,num//2+1):
  if num%i==0:
     prime=False
     break
  
if prime:
    print("it's prime num")
else:
    print("it's not a prime num")