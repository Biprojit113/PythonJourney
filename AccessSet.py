"""
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.


"""
A ={'Are', 'You', 'There', 'How', 'Hello'}
 #It looped through the whole set and then printed it (remember we cann't use index or key)
for i in A:
    print(i)

print("How" in A) #True
print("LOL" in A)#False
