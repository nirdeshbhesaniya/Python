class calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"The square of {self.n} is {self.n ** 2}")
    def cube(self):
        print(f"The cube of {self.n} is {self.n ** 3}")
    def square_root(self):
        print(f"The square root of {self.n} is {self.n ** 0.5}")
        
c = calculator(4)
c.square()  
c.cube()
c.square_root()
        