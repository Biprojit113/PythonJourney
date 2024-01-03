
hey = helo= hi = "All together"
h,ho,hk = "You","are","awesome"
h,ho,hk = "IT", "is", 4
x = 23
y = 23.567
z = "Hello"
a,b,c = 12,23,45
h
#a varriable containing many parts
#python allows to unpack those package
family = ["me","myfather","mymother","mysisters"]
#now unpacking the family package
#by adding varriables to those items
o,p,q,l = family

print (x)
print(y)
print(z)
print (hey)
print(helo)
print(hi)
print (a,b,c)
"""
the best way to print multiple values in python is by using comma's instead
of +
"""
print(h,ho,hk)
"""
other way
can't print value and string together
print(h + " "+ ho + " " + hk)  #TypeError: can only concatenate str (not "int") to str  """

h,ho,hk = "You", "are", "awesome"
print(h + " "+ ho + " " + hk)


print (o)
print(p)
print(q)
print(l)

#hey its a comment
"""
for print in iteration/condition
there needs to be an indention(gap)
before print
"""

if 9>4 :
    print ("9 is greater than 4")
