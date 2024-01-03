"""
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
a “chunk” of code that you can use over and over again, rather than writing it out multiple times

In Python, you define a function with the def keyword, then write the function identifier (name) followed by parentheses and a colon.

To call this function, write the name of the function followed by parentheses:


From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.

"""

def createFunction(x,y) :       #####Here x and y are parameters
    print("The function is created in python")
    x = x+y
    print(x)
    

#To call this function, write the name of the function followed by parentheses:
createFunction(23, 56)   # 23, 56, 24, 34, etc is the arguments 
createFunction(24,34)
createFunction(78,67)


"""
From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.

"""


def names(Firstname):
    print(Firstname +"  "+ "Helen")


names("Robert")
names("Morgan")
names("James")

#If you try to call the function with 1 or 3 arguments, you will get an error:

def help(x,y):
    print(x,y)

##help(78)      #help() missing 1 required positional argument: 'y' Error

##If the number of arguments is unknown, add a * before the parameter name:

def name (*people):         #people: parameter name
    print(*people[2],*people)


name("Helen", "Rubina", "Lucas")
#       0        1         2


"""
Keyword Arguments
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.

"""

def industry(veh1,veh2,veh3):
    print("THe industry has"+ " " + veh3)

industry(veh1 = "Cars", veh2 = "bikes", veh3 = "Airplanes") # now the ordered state is not needed #veh1[1]


"""
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, 

"""

def locals(**village):
    print("Locals are" + " " + village["people"] + village["animals"])

locals(people = "REguklar", animals = "Old", trees = "Cared" )


# *args name refers unlimited arguments can be added in that function 
# **args name refers there is unlimited arguments with their keyword can be added


"""
Default parameter value

If we call the function without argument, it uses the default value:

"""
def family(member = "Jammy"):
    print(member)


family("Tina")
family ("Robin")
family()  # Jammy  (default value) everytime some arguments stays default if we don't was to use them and they stay default and won't affects our code until we give them a value
family("Mother")
family("Father")


def add(x = 0,y = 0,c= 0): #default value is 0
    print(x+y+c)

add(23,45)
add(34,56,77)
add(56,34)
add(30)
add()



def good(foods):
    for i in foods:
        print(i)

fruits=["Apple","Mango", "banana", "jackfruit"]   #list
fruit = ("blackberry", "Mango")  #tuple
good(fruits)
good(fruit)

def goods(dictio):
        for x in dictio:
            print(x)
            print(dictio[x])
        y = dictio.items()
        print(y)
       


basic = {
    "Food": "100%",
    "Shelter": "100%",
    "Education" : "100%"
} 

goods(basic)

#To let a function return a value, use the return statement:


def adds(x,y):
    print(x,y)
    return x+y
    
def sub(x,y):
    print(x,y)
    if x>y:
        return x - y
    elif x<y:
        return y-x
    else: print("Please input 2 number")

x = adds(20,30)
print(x)
print(adds(34,45))
print(sub(320,520))
y = sub(50,20)
print(y)
z = sub(40,40)  
print(z)

def mul(x):
    return 2*x

for i in range(10):
    x = mul(i)
    print(x)

def fun():  #if we want to take the function as empty need to use pass to avoid errors
     pass
fun()








