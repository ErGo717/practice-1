class Person:
    def init(self,name):
        self.name = name
        
class Student(Person):
    def init(self, name, gpa):
        super().init(name)
        self.gpa = gpa
    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")
        
name , gpa = map(str,input().split())
gpa = float(gpa)
student = Student(name, gpa)
student.display()