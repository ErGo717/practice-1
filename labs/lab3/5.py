class Shape:
    def area():
        return 0
    
class Square(Shape):
    def init(self,n):
        self.length = n
        
    def area(self):  
        return pow(self.length, 2)
    
n = int(input())
s1 = Square(n) 
print(s1.area())