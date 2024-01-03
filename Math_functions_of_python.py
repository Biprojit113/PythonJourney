#The min() and max() functions can be used to find the lowest or highest value in an iterable:

x = min(34,45,42,2,66,5,0)
y = max(234,4355,56546,566,543,443,43545)

print(x)
print(y)

#The abs() function returns the absolute (positive) value of the specified number:

s = -439
s1 =abs(0)
s2 = 45 - 79
print(abs(s))
print(s1)
print(abs(s2))  #in normal logic answer should be -34 but for absolute that means always + the value is 34

#The pow(x, y) function returns the value of x to the power of y 

f = pow(4,5) #4*4*4*4*4 = 1024
f2 = pow(2,0)

print(f)
print(pow(4,5))
print(f2)

#Python has also a built-in module called math, which extends the list of mathematical functions
import math #math module imporing

print(math.sqrt(169)) #  13^2 = 169 --> square root of  13^2 = 13

a = math.sqrt(64)
print(a)

#The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

k = math.ceil(1.554656)
k1 = math.floor(1.554656)
print(k)# 2 cause 1.5 is greater closest integer value is 2
print(k1)# 1 cause 1.5 is lower closest integer value is 1

#the math.pi module gives the constant pi number

p = math.pi
print(p)
