
"""
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator:

"""
#Return an iterator from a tuple, and print each value:


k = ("locals", "never", "misjudge")

m = iter(k)  #_iter_ method iterates the value 

print(next(m))     #next method to print the iterated value 1 by 1     
print(next(m))
print(next(m))

for i in k:
    print(i)


#Even a string can be iterated by iter()method

k = "Hello"

stri = iter(k)

print(next(stri))
print(next(stri))
print(next(stri))
print(next(stri))
print(next(stri))

#The for loop actually creates an iterator object and executes the next() method for each loop.
for i in k:
    print(i)

"""
Create an Iterator

The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

The __next__() method also allows you to do operations, and must return the next item in the sequence.
"""


#Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


class myclass:
   def __iter__(self):   # for the starting value of itration answers the q of where to start
      self.x = 2
      return self
   def __next__(self):  #goes for the next value answers what will be the next value 
      x = self.x
      self.x *= 2
      return x

myobj = myclass()
iterate = iter(myobj)
print(next(iterate)) 
print(next(iterate))
print(next(iterate)) 
print(next(iterate)) 
print(next(iterate)) 
print(next(iterate))  
print(next(iterate)) 



##### Stop iteration by adding condition

"""
StopIteration statement
The example above would continue forever if you had enough next() statements, or if it was used in a for loop.

To prevent the iteration from going on forever, we can use the StopIteration statement.
"""
class change:
   def __iter__(self):
      self.val = 1
      return self
   def __next__(self):
      s = self.val
      if self.val<=20:
         self.val += 1
         return s
      else: 
        raise StopIteration  # using the StopIteration statement


obj = change()
it = iter(obj)


for x in it:
   print(x)
