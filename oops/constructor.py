class student :
    def __init__ (self , name=None,rollNo=None,age=None):
        self.name=name
        self.rollNo=rollNo
        self.age=age
    def show(self):
        print(f"name = { self.name}")
        print(f"rollNo = {self.rollNo}")
        print(f"age = {self.age}")

stu1 = student("Rohit",564)
stu2 = student("Rahul",510)
stu3 = student("Mohit",520,26)

stu1.show()
stu2.show()
stu3.show()
    