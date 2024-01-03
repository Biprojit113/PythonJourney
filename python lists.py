               ########### Access List Items \\\\\\\


fruits = ["Apple", "Mango", "Banana"]

print(fruits[-2])

fruits1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(fruits1[2:5])

fruits2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(fruits2[:4])

fruits3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(fruits3[2:])
fruits4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(fruits4[-5:-3]) #the value of left side must be bigger than the right side in this process cuz without the base how the code could climb up


frut = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

if "banana" in frut:
    print("yes,banana is present in the fruit list")
else:
    print("It isn't listed yet!!!")
     

                            ######## Change List Items |||||||


th =  ["Apple", "Pineapple", "Jackfruit"]

th[1] = "banana"
print(th)


th =  ["Apple", "Pineapple", "Jackfruit"]
#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
th[1:3] = ["banana"]
print(th)

# to insert an item just use insert funtion
th = [ "Apple", "pineapple"]
th.insert(2, "watermalone")
print(th)


                        #### Add an item to the list //////

# append to add at last 
#insert to add with specified position
#extend to add values from another lists (tuples, sets, dictionaries etc.)

hi =  ["how", "are", "you!!!"]

ko =  "wassup"


hi.append(ko)

print(hi)

hi.insert(0,"Hey!")
print(hi)

lo =  ["how","are", "you", "doing"]
l = ("take", "care")
l = "Hello", "There"

hi.extend(lo)
print(hi)

hi.extend(l)
print(hi)

                      ##### Remove from list /////

# remove() removes specified string
# pop() can delete the specified index
# del will also the index and also the list
# clear() will empty the list



re =  ["Hu", "ki", "ko"]

re.remove("ko")
print(re)
re =  ["Hu", "ki", "ko"]

re.pop(1)
print(re)

re =  ["Hu", "ki", "ko"]
re.pop()
print(re)

re =  ["Hu", "ki", "ko"]

del re[0]
print(re)
re =  ["Hu", "ki", "ko"]
del re   # to delete full list

re =  ["Hu", "ki", "ko"]

re.clear()
print(re)  #[]

                       
                        ####  Loop List   \\\\\

# Print all items in the list, one by one:
kk = ["Call", "send", "input"]
for i in kk:
    print(i)

# Print all items by referring to their  just index number:
koli = ["Call", "send", "input"]
# range helped to gather the range (0 to 2), len helped to identify the total number of values and k is going to print the 0 to 2 by looping
for k in range(len(koli)):
    print(k)

# Print all items, using a while loop to go through all the index numbers

kol = ["call", "dad", "now"]

i = 0
while i<len(kol):
    print (kol[i])
   
    i = i + 1



                      



