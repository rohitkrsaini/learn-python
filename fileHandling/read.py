files = open("demo.text","r")
print(files.read())
files.close()

# with key words
with open("demo.text", "r") as readFile:
    print(readFile.read(3))
    print(readFile.readline())
    readFile.seek(0)
    list = readFile.readlines()
    print(list)
    