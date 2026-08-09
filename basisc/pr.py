# # Parent Class
# class Animal:

#     def sound(self):
#         print("Animal makes a sound")


# # Child Class
# class Dog(Animal):

#     def bark(self):
#         print("Dog barks")


# # Object
# d = Dog()

# d.sound()   # Parent class method
# d.bark()    # Child class method

from array import array
# second larset
arr = [10, 20, 30, 40,86,34,58,93,38,68]

print(arr)
arr.sort()
print(arr[-2])
# remove duplication
arr = [ 1,2,2,3,3,4,4,5,6,7,8]
print(list(set(arr)))

# two sum

arr = [ 2,3,7,4,6,1,8]
target = 9
for i in range((len(arr))):
    for j in range(i+1 ,len(arr)):
        if arr[i] + arr[j] == target: 
         print(i,j)