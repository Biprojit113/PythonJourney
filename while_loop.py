"""
Python has two primitive loop commands:

while loops
for loops


"""

#Print i as long as i is less than 6:

i = 0

while i<6 :
    print(i)

    i = i+1

#break statement we can stop the loop even if the while condition is true:

i = 1
while i<6 :   #condition
    print(i)    #value
    i +=1        #increement
    if i  == 4 :
        break # to break the loop it won't iterate after 4
    
      


#continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#else statement we can run a block of code once when the condition no longer is true:

else:        # to print just a message after all condition ha been fullfilled
   print("i is no longer less than 6")
