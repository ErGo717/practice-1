# Math and random operations

#1.
import math
deg = float(input("Input degree: "))
rad = deg * math.pi / 180
print("Output radian:", f"{rad:.6f}")


#2.
h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))
area = (a + b) / 2 * h
print("Expected Output:", area)


#3.
import math
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
area = (n * s**2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", area)


#4.
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = base * height
print("Expected Output:", area)