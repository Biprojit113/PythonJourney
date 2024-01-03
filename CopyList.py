# We cannnot copy a list by simply typing List2 = list1 cuz list2 always holds the value of list1 it won't change 

# to copy a list
man = ['Accessories', 'Education', 'Foods', 'Safety', 'Shelter']

man2 = man.copy()  #copy method
print(man2)

man2 = list(man)  # entering the value of man list into the list of man2 using list method another way to copy
print(man2)