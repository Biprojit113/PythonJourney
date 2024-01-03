
x = "global Varriable"
"""
global varriable always declared outside
we can use it anywhere
"""
#def is used to declare a function datatype
def functionName():
    '''
        if there x is decclared inside function then the output
        inside this function will be this value no global value
    '''       
    '''
    if we want to use that value as global value then we need to use global keyword
    '''
    #calls global scope
    #global x
    x = "function"
    
        # if there is no varriable declared inside this function then the value
        # will print global varriable
    print("It's a" +" "+ x)  

#recaling the function
functionName()

print(x)
