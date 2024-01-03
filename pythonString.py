
#printing a paragraph in string datatype

a = """Hello Everyone i thought you  wouldn't miss me but all on a sudden i was right that i can't believe. Rightly guys you are all awesome but you are all i think lacking some composure. It's not a mandatory site but yeah it's important i would like to have it in us
    By the way guys how was your trip. I hope it gone well i can imagine how much fun you guys had. I hope i had the same but my father was sick and i can't left him alone. I think i am saying sad stuff. Let me know guys how was my paragraph.
    """
print(len(a))


print(a)
print('thought' in a)  #boolean result true / False

print('miss' not in a)  #boolean result true / False
if 'took' in a:
  print("It is in there")
else:
  print("it is not there")
#python slicing  
print(a[0:6]) # to print from 0 index to index 5
#slice from the start
print(a[:7])
#slice to the end
print(a[19:])

print(a[0:5] + " "+ a[6:14])



#Using negative indexes to start from the end decreement
l = "wow you guys are awesome"
print(l[-11:-8]) #result: are

k = 'Hello hi'
print(k.strip()) #to clear spaces at the begining or at the end strip()
print(k.upper()) #getting all uppercase string
print(k.lower()) #getting all lowercase string

print(k.replace('e','k')) #replacing string values result Hkllo in place Hello
print(len(a))


#formatting
age = 44
t = "my age is {}" #can declare an global integer by adding them as the element of an array
print(t.format(age))#to format the string

for a in 'bamboo' :
    print(''+ a)
    
    
    
