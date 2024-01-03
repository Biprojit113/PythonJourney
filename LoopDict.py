inside = {
   "Sports" : "Cricket",
   "Country" : "Bangladesh",
   "Born"   : 1975,
   "Tropies" : None
}
#Print all key names in the dictionary
for i in inside:
    print(i)

#Print all values in the dictionary
for i in inside:
    print(inside[i])


#values() method to return values of a dictionary:
for i in inside.values() :
    print(i)

#keys() method to return the keys of a dictionary:
for x in inside.keys():
    print(x)

#both keys and values, by using the items() method:
for x in inside.items():
    print(x)

i = 0

while i < len(inside):
    print(i)
    i += 1
