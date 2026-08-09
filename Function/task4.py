list = ["rohit,mohit,anshul,Rahul,lakshya"]
upperCase = []
for i in list:
    upperCase.append(i.upper())
print(upperCase)

#list comphestion
uppCase = [x.upper() for x in list]
print(upperCase)

# function
def uppCas(list):
    upp = [ y.upper() for y in list]
    return upp
print(uppCas(list))