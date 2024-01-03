human = ["Foods", "Shelter", "Education", "Accessories", "Safety"]

human.sort()    #assending according to the letter
print(human)
Inhuman = ["Foods", "Shelter", "education", "Accessories", "safety"]
Inhuman.sort()
print(Inhuman)           # in casesensitive (combined with lower and upper(F,S,A and e,s))the sort method gives an unexpected results
Inhuman.sort( key = str.lower) # to solve casesensitive issue we use a varriable and withing the str.lower
print(Inhuman)
value = [100,200,23,45,56,67]
value.sort()

print(value)
human.sort(reverse = True) # desending 
print(human)

human.reverse() # to reverse the whole value in reverse order
print (human) 

def humana(n) :
    return abs(n-50)

value = [100,200,23,45,56,67]
value.sort(key = humana)
print (value)
