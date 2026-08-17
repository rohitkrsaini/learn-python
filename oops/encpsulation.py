class stu:
    def __init__(self):
        self.__name = ''

    def get_name(self):
        print(self.__name)

    def set_name(self, name):
        self.__name = name


s = stu()
s.set_name("rohit")
s.get_name()