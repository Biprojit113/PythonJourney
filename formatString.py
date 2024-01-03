'''
Here if we use string with numbers then it won't print will show errors
so we need to use format'''
s = 22
p =  "Hello"

print(p + format(s))

#multiple

t = 33
r = 35.4564
k = 8778

o = "I want {} pieces of {} kangaru in the format of {}"

print(o.format(t,r,k))

#Escape Character(\',\\,\n,\r,\t,\b,\f,\ooo,\xhh)

txt = 'Hello ladies and\'Gentlemen\' How are you'
txt = "Hello ladies and\"Gentlemen\" How are you"
txt = "Hello ladies and\n \"Gentlemen\"\n How are you"
txt = "Hello ladies\\ and\"Gentlemen\" \\How are you"
l = 'Hello ladies \band\'Gentlemen\' How are you'

print(txt)
#l = 'Hello\rthere'
print(l) 
#A backslash followed by three integers will result in a octal value:
x = "\110\145\154\154\157" #Hello
print(x)
#A backslash followed by an 'x' and a hex number represents a hex value:
lo = "\x48\x65\x6c\x6c\x6f" #Hello
print(lo) 
