#access the items of a dictionary by referring to its key name, inside square brackets:

inside = {
   "Sports" : "Cricket",
   "Country" : "Bangladesh",
   "Born"   : 1975,
   "Tropies" : None
}

print(inside["Sports"])
#using get() method

k = inside.get("Country")
print(k)

#using keys() method toget all the keys

k = inside.keys()
print(k)

#using values() method to get only values

l = inside.values()
print(l)

# Adding a key with values
k = inside.keys()

inside["Format"] = 3  #will add at last of inside dictionary
print(inside)


# updating a value

k = inside.values()

inside["Tropies"] = 1
print(inside)
l  = inside.values()
print(l)

inside["Born"] = 1979
print(inside)
l = inside.values()
print(l)

#using items() method to get items of the dictionary all items 
p = inside.items()
print(p)
inside["First played"] = "England"
o = inside.items()
print(o)

if 'Born' in inside:
    print("yes it has born")
