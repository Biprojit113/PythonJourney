
a = "eubbeR roy aru"
b = "hello my dear my love my world!"
c = "hello Stale"

print(a.capitalize())
print(a.casefold())
print(a.center(20))
print(a.center(20, "H"))
print(b.count("my"))
print(b.count("my",10,30))
print(a.encode())
print(b.endswith("!"))
#print(a.endswith("u"))
v = "H\te\tl\tl\to"

print(v.expandtabs(5))

t = "Hi How are you It's a beautiful world to live on, don't you think."

print(t.find("live"))
print(t.find("u", 5, 15))
print(t.find("j"))#returns -1
#print(t.index("j"))#describe error

lo = "Hello there how's your store price {price:.2f}" #for decimal number

print(lo.format( price = 444))

loo = "Hello there how's your store  {price:<8}  price"#8 space to the right

print(loo.format (price = 88))

loo = "Hello there how's your store  {price:>8}  price"#8 space to the left

print(loo.format (price = 88))

loo = "Hello there how's your store  {price:^8}  price"#8 space to the center

print(loo.format (price = 88))

loo = "Hello there how's your store  {:=8}  price"#8 place the sign to the left mot position

print(loo.format (-88))

loo = "The temperature is between {:+} and {:+} degrees celsius."
print(loo.format(-7,6))

lu = " The Universe is {:,} years old " # thousand separator ,

print(lu.format(1300000000000000))

lu = " The Universe is {:_} years old " # thousand separator_

print(lu.format(1300000000000000))

lu = " The Universe is {:b} years old " # binary format

print(lu.format(10))


lu = " The Universe is {:e} years old " # scientific lower format

print(lu.format(10))

lu = " The Universe is {:E} years old " # scientific Capital format

print(lu.format(10))


lu = " The Universe is {:G} years old " # general format

print(lu.format(19))

lu = " The Universe is {:o} years old " # octal format

print(lu.format(19))

lu = " The Universe is {:x} years old " # Hex format

print(lu.format(19))










