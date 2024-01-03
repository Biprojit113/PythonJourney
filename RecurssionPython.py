"""
Recursion is a common mathematical and programming concept. It means that a function calls itself.
 This has the benefit of meaning that you can loop through data to reach a result.
To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

"""


# Using a World Famous Example of recursion factorial !

def factorial(n):
    #base case cause we need to use a condition to stop the recursion
    if(n==1):
        return 1
    else:
        return n * factorial(n-1)    #calling the function inside the function
    

x = factorial(5)
print(x)

def val(n):
    if n == n/2:
        print("iteration in its midstage")  
        
    elif n == 0:
        print("Iteration is complete")
    else: 
        return val(n-1)
       
        

val(9)





def v(k):
    if (k > 0):
     i = k + v(k-1)
     print(i)
    else:
        i =0
    return i
    
print("//RECURSION VALUE=======")

v(9)

#another way to find factorial i made it bruhhh that was awesome
def mult(n):
    if (n>0):
        return n * mult(n-1)
    else:
        mul = 1
    return mul

print(mult(5))  #120

