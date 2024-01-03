
lis = ["Human", "Eats", "Meat"]

for x in lis:
    print(x)

#Looping Through a String

for x in "Hello":
    print(x)

#With the break statement we can stop the loop before it has looped through all the items:

for x in lis:                       #before break print
    print(x)
    if x == "Eats":
        break


for x in lis:
    if x == "Eats":
        break
    print(x)                             #after the break print only human

#With the continue statement we can stop the current iteration of the loop, and continue with the next:
#Do not print Eats:
for x in lis:
    if x == "Eats":            
        continue
    print(x)                #Eats won't be in the output list

#range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(8):   #Here the range is 0 to 7
    print(x)

#however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6) And also the increement value as its default state is 1:

for x in range(3,6):
    print(x)

#also changing the increement
# also using else to printout the message after the loop has been finished

for x in range(3, 27, 3):
    print(x)

else:
    print("Work here is done for now...........")

# Note: The else block will NOT be executed if the loop is stopped by a break statement.

for x in range(8):
    if x == 6:
        break
    print(x)
else :
    print("Code is failed to compile you LOL (' - ')")  #So after break the else statement won't work because the loop isn't meet its conditions yet




#Nested Loops

kali = ["They", "are", "needy"]

for x in lis:
    for y in kali:
        print(x,y)          #One loop is inside an another loop





#pass statement to avoid getting an error. for some reason if we make the loop empty
for x in range(5):
    pass




