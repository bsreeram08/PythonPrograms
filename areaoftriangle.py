import math
a=int(input("Enter the first side of triangle:"))
b=int(input("Enter the second side of triangle:"))
c=int(input("Enter the third side of triangle:"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print "Area of triangle is :"
print  area
