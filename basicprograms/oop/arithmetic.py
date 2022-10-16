class arithmetic:

    def __init__(self,a,b):
        self.n1=a
        self.n2=b
    def arith(self):
        print(f"addition:of {self.n1} and {self.n2} is {self.n1+self.n2}")
        print(f"subtraction:of {self.n1} and {self.n2} is {self.n1-self.n2}")
        print(f"multiplication:of {self.n1} and {self.n2} is {self.n1*self.n2}")
        print(f"division:of {self.n1} and {self.n2} is {self.n1/self.n2}")


a=arithmetic(3,2)
a.arith()
