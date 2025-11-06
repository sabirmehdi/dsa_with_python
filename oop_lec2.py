class point():
    def __init__(self,x=0,y=0, z=0):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return "["+str(self.x) + ","+ str(self.y)+ ","+str(self.z)+"]"


p1=point()
p2= point(3,4,5)
print("This is value of P1 (x): ",p1.x)
print("This is value of x, y: ",p2)



