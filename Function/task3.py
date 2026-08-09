# add correponding elements

l1 = [1,2,3,4,5,6]
l2 = [6,5,4,3,2,7]

def addCorrespon(l1,l2):
    finalList = []
    for x,y in zip(l1,l2):
            finalList.append(x+y)
    return finalList

print(addCorrespon(l1,l2))

# list comphesition

def addCorr(l1,l2):
      finalL = [ x+y for x,y in zip(l1,l2)]
      return finalL
print(addCorr(l1,l2))