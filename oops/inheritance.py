class electonicDevice:
    def powerOn(self):
        print("power On")

class laptop(electonicDevice):
    def code(self):
        print("start coding")

device = laptop()
device.powerOn()
device.code()

# mutlilavel

class vechicl:
    def start(self):
        print("start car")

class car(vechicl):
    def drive(self):
        print("drive a car")

class ev(car):
    def musics(self):
        print("play musics")

v = ev()
v.start()
v.drive()
v.musics()