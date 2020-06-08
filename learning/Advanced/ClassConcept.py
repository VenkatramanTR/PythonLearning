class Computer:
    def __init__(self,cpu, ram):
        print("init method")
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("config is ", self.cpu , self.ram)

com1 = Computer("i5","8gb")
com2 = Computer("i7","16gb")

# first way of calling
#Computer.config(com1)
#Computer.config(com2)

# second way of calling
com1.config()
com2.config()