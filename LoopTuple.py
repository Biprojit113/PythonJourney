td = ('Someday', 'People', "Won't", 'Remember', 'You')

for i in td:
    print(i)
"""
printing the values of td
Someday
People
Won't
Remember
You
"""

# printing the values according to their index number
# by using range() and len()

for i in range(len(td)):            # first finding the length = 5 and then the range between 0 to 4 now i is 0 and but less then 5 then print 0 likewise 1,2,3,4 
    print(i)

i = 0
while i< len(td):
    print(td[i])  #td[] cause the tuple is stored or inputed in array type 
    i += 1

