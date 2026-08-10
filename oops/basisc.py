class mobilePhone :
    def mobile(self,brand ,prices):
        self.mobile = brand
        self.value = prices

    def show(self):
        print(f"brand name is = { self.mobile }\n value is = { self.value} ")

obj = mobilePhone()
print(obj.mobile("moto",15000))  
print(obj.show())