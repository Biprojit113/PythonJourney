#Note: Both union() and update() will exclude any duplicate items.

# Union()method

C = {1, 'There', 'You', 'Hi', 11, 'Are', 'Hello', 'How'}
C1 = {1,2,4,5}

x = C.union(C1)
print(x)

# update()
C = {1, 'There', 'You', 'Hi', 11, 'Are', 'Hello', 'How'}
C1 = {1,2,"Eww"}
C.update(C1)
print(C)