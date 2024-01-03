"""
lambda functions are one line operation 
lambda function is a small function, not too powerfull but fast
very essential while using a function inside a function
A lambda function is a small anonymous function.  that means it doesn't need any names like all other function

Python Lambda Function Syntax

Syntax: lambda arguments : expression

"""

def add(x):
    return 5*x

print(add(5))

# for lambda function

print((lambda x : 5*x)(3))

# We can assign the lambda function

x = (lambda x: x*x*x)        
#    argument(x) :  expression(x*x*x)
print(x(3))

# we can add as much as arguments we want in lambda function

x = (lambda a,b,c: (a+b)**2-(2*a*c))

print(x(23,42, 56))   # 9 with 2 arguments a,b and c

# The power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number
#Use that function definition to make a function that always doubles the number you send in:

def val(n):
    return lambda a: a * n    # here a is an unknown number
#                 7: 7 * 2 = 14 

double = val(2)  # val is the mai function    and double is the anonymous function (lamda) take inputs
print(double(7))

# Now for finding the triple of that number

def valu(n):
   return lambda x: x * n

triple = valu(3)
print(triple(6))


# to find cube of a list every number

def val(func, iter):
    result = []
    for x in iter:
        newitem = func(x)
        result.append(newitem)
    return(result)
    

v = [23,2,4,5,5,6]


cubed = val(lambda x : x**3 , v)

print(cubed)




