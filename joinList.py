#append = add (something) to the end of a written document. extend = adding extra matter
lol = ['Accessories', 'Education', 'Foods', 'Safety', 'Shelter']
lol2 = ['Family', 'Curricullam']

lol = lol + lol2      # normal
print(lol)


lol = ['Accessories', 'Education', 'Foods', 'Safety', 'Shelter']
lol2 = ['Family', 'Curricullam']
for x in lol2:
    lol.append(x)

    print(lol)
lol = ['Accessories', 'Education', 'Foods', 'Safety', 'Shelter']
lol2 = ['Family', 'Curricullam']

lol.extend(lol2)  # cann't use append here cause append works with only list but extend works with string
print(lol)
