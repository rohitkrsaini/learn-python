# def check_auth(func):
#     def wrapper():
#         print("checking...")
#         func()
#     return wrapper

# @check_auth
# def dasbord():
#     print("welcome to dashbord")
# dasbord()

text = "i love my india"
result = " ".join(text.split()[::-1])
print(result)
print(text.count("i"))

fre = {}

for char in text:
    if char != " ":
        if char in fre:
            fre[char] += 1
        else:
            fre[char] =1
for key,vale in fre.items():
    print(key," : " ,vale)