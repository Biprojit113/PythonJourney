a = 100
b = 50

if b > a:
    print("b is greater than a")

else :
    print("a is greater than b")

 #The bool() function allows you to evaluate any value, and give you True or False in return,

print(bool({}))
print(bool(12))
print(bool([]))
print(bool(0))
print(bool("Hello"))

bool(["apple", "cherry", "banana"])

bool(0)
bool({})

class myobj():                     #within a class
    def len (self):                 #within a function
     return 0
    
myclass = myobj()
print(bool(myclass))



def myfunc():
    return True

print(bool(myfunc))

def myfunc():
    return False


if myfunc():
    print ("Yes!")             #if the func returns true
else :
    print("No!")                     #if the func returns false


x = 43454

print(isinstance(x,int))        #if the varriable is integer or not






