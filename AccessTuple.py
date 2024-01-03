
# the tuple stores data in ordered so it stays within its index

tup = ("Someday","Even", "People", "Won't", "Remember","You")
#         0         1        2        3          4       5     starts with 0  left to right
#         -6        -5       -4       -3        -2       -1      starts with -1 from right to left
print(tup[4]) #remember

#Negative indexing 

print(tup[-2]) #remember
#print people won't

print(tup[2:4])

#print people won't in negative indexing

print(tup[-4:-2])

# print 3 string but not 4

print(tup[:3])

# print from index 2/ string 4 to last

print(tup[2:])
print(tup[3:])

if "Even" in tup:
    print("It exits!!!")
else :
    print("It isn't here!!!")    

############ REMEMBER PYTHON IS Case Sensitive !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
if "even" in tup:
    print("It exits!!!")
else :
    print("It isn't here!!!")    