# age = eval(input("enter the age : "))
# print(age,type(age))

# if (age>=18):
#  print("yes")
#  print(age)
 
# caluleter

val1 =eval(input("enter the num"))
val2 = eval(input("enter the num"))
userCh = input("enter the opreter")

match userCh :
 case'+':
  print(val1+val2)
 case'-' :
  print(val1-val2)
 case'*':
  print(val1*val2)
 case _:
  print("invaildOP")