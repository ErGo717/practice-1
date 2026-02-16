class Shape:
    def area():
        return 0

class Circle(Shape):
    def init(self, r):
        self.radius = r
        
    def area(self):  #override
        return 3.14159 * pow(self.radius , 2)
    
r = int(input())
circle = Circle(r)
print(f"{circle.area():.2f}")