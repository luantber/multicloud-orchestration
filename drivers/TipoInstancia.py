class TipoInstancia():
    def __init__(self,name=None,cpu=None,ram=None,price=None,free=None):
        self.cpu = cpu
        self.ram = ram
        self.price = price
        self.free = free
        self.name = name

    def describe(self):
        cadena = "name: " + self.name + "\ncpu:" + str(self.cpu) + "\nram:" + str(self.ram) + "\nprice: " + str(self.price) 
        cadena += "\nfree:"+ str(self.free)
        print(cadena+"\n")


        