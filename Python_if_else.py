"""
python supported logical conditions
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b


"""

a = 98
b = 98


if a>b:
    print(a ,"is greater than" , b)

#elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition". its the similar as else if in c
elif a==b :
    print("a are equal to c") 
   
else :
    print(b , "is greater than" , a)


a = 34
b = 35

if b>a : print("b is greater than a")


#Short Hand If ... Else
print("A") if a>b else print("B")

c = 35
d = 35
#multiple else statements on the same line

print("A") if c>d else print("B") if c == d else print("=")   #No need to use this method if you do the you are dumb bruhhh

#and keyword is a logical operator, and is used to combine conditional statements:
if a<b and b==c :
    print("The statement is True!!!")

#or keyword is a logical operator, and is used to combine conditional statements:
if a>b or b==d :
    print("The statement is definately True!!!")

else :
    print("bro you gotta look again!!")



#not keyword is a logical operator, and is used to reverse the result of the conditional statement:

if not a>b:
    print("No a is less then b")


#Nested If

if a > 20:
    print("a is greater than 20")
    if a > 30 :
        print("a is also greater than 30")

else :
    print("a is not greater than 30") 


    #pass Statement to avoid error while having a empty if else


if a>a :
    pass   # to pass the if else statement



