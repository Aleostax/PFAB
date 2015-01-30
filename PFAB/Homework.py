#!python
import math
first = "Adam"
last = "Barnhill"
age = 35
print "Author: ",first,last,"age: ",age
sideA = 12.55
sideB = 17.85

x = (sideA*sideA) + (sideB * sideB)
x = math.sqrt(x)
print "sideC is ",x

op1 = 95.0
op2 = 64.5

def compthis(y,z):
	print "Function Adds, subtracts, multiplies, divides and performs modulus between two variables\n\tCurrent values are:",y,"and ",z,"\n"
	print "sum:",y+z,"diff:",y-z,"Mult:",y*z,"div:",y/z,"Mod:",y%z

compthis(op1,op2)
