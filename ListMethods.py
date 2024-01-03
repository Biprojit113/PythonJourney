#\\\\\  append()  method  //// Adds an element to the end of the list.
      #list.append(elmnt)
#elmnt  ---->>>>  Required An element of any type (string, number, object etc.)
Lis = ["kebra", "baba","pagla"]

Lis.append("baba")
print(Lis)

"""
          \\\\\  clear() method  ////
  clear() method removes all the elements from a list
       list.clear()
"""

l = ['kebra', 'baba', 'pagla', 'baba']
l.clear()
print(l) # [] empty

"""
         \\\\\  copy() method  ////
      copy() method returns a copy of the specified list
             list.copy()

"""
k = ['kebra', 'baba', 'pagla', 'baba']
k2 = k.copy()

print(k2) # copied K to K2

"""
              \\\\\  copy() method  ////
    count() method returns the number of elements with the specified value
    list.count(value)
    value ---->>>>  Required An value of any type (string, number, object etc.)
 
"""
p = [100,909,909,93,930,"Hello"]

m = p.count(909)   # needs to put the iterative value in some varriable Important issue
print(m)
n = p.count("Hello") 
print(n)


"""
              \\\\\  index() method  ////
    index() method returns the position of the specified value.
       list.index(elmnt)  
    elmnt ---->>>>  Required An value of any type (string, number, object etc.)
 
"""
j = ['kebra', 'baba', 'pagla', 'baba']
#       0       1        2        3
l = j.index("pagla")
print(l)  #2


"""
              \\\\\  insert() method  ////
    insert() method inserts the specified value at the specified position.
    list.insert(pos, elmnt)
    pos---->>>>  Required. A number specifying in which position to insert the value
    elmnt ---->>>>  Required An value of any type (string, number, object etc.)
 
"""
h = ['kebra', 'baba', 'pagla', 'baba']
h.insert(2, "betala")    # added a value but didn't replace it remember
print(h)


"""
              \\\\\  pop() method  ////
    pop() method removes the element at the specified position.
    list.pop(pos)
    pos---->>>>   Optional. A number specifying the position of the element you want to remove, default value is -1, which returns the last item
    
"""
o = ['kebra', 'baba', 'betala', 'pagla', 'baba']
o.pop(2)#3 no element is deleted
o.pop()  #last element is deleted
print(o)

"""
              \\\\\  remove() method  ////
    remove() method removes the first occurrence of the element with the specified value.
    list.remove(elmnt)
    elmnt ---->>>>  Required An value of any type (string, number, object etc.)
 
"""

o = ['kebra', 'baba', 'betala', 'pagla', 'baba']

o.remove("betala")
print(o)

"""
              \\\\\  reverse() method  ////
    reverse() method reverses the sorting order of the elements
    list.reverse()
 
"""
o = ['kebra', 'baba', 'betala', 'pagla', 'baba']
o.reverse()
print(o)

"""
              \\\\\  sort() method  ////
    sort() method sorts the list ascending by default.
     list.sort(reverse=True|False, key=myFunc)
    reverse ---->>>>	Optional. reverse=True will sort the list descending. Default is reverse=False
    key	 ---->>>> Optional. A function to specify the sorting criteria(s)
 
"""
# A function that returns the 'year' value:
def myFunc(e):
  return e['year']       #sorting according year assending
 
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key = myFunc)
print(cars)


# A function that returns the length of the value:
def myFunc(e):
  return len(e)

car = ['Ford', 'Mitsubishi', 'BMW', 'VW']

car.sort(reverse=True, key=myFunc)
print(car)