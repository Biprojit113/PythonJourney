# In python we can also unpack the values assigned to tuple 

tupl = ("Some", "things", "Never", "Changes")
(so, what, are, you) = tupl      #decalring the varriables for tuple tupl values like some as so and so on

print(so)
print(what)
print(are)  
""" Some
things
Never
"""

# '*' -> it means asterisk it uses to assign rest values as a list 
tupl = ("Some", "things", "Never", "Changes","True")
(so, what, *are) = tupl   # now the *are will assign never, and the rest as a list because there is not enough variables as values
print(so)
print(what)
print(are)  #['Never', 'Changes', 'True'] list

(so, *what, are) = tupl  # in this case pytho will print all strings from 2nd fast to 2nd last
print(so)
print(what)
print(are)