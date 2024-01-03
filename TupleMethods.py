"""
///// ///// ////  count() method |||||||||||||
count() method returns the number of times a specified value appears in the tuple.
tuple.count(value)
value	Required. The item to search for

"""

tu = ("Hello", "There", 1, 1, 11, 11, 1, 11, 1)
x = tu.count(1)  #how many times the 1 is there in the tuple
print(x)

"""
///// ///// ////  index() method |||||||||||||
index() method finds the first occurrence of the specified value.
tuple.index(value)
value	Required. The item to search for

"""

tu =  ("Hello", "There", 1, 1, 11, 11, 1, 11, 1)
y  = tu.index(1)  #to find the index value of that searched value
print(y)

