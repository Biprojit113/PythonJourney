
#Create a dictionary that contain three dictionaries

inside = {                           #first have to change the dict names into a string "" then : then {} inside will be the keys at end a , 
   "Sports" : {
       "Cricket" : "international",
       "Football" : "Same"
   },
   "Country" : {
       "Bangladesh": "Regular",
       "UK" : "NotRegular"
   },
   "Born" :{
       "year":1975,
       "year1" : 1979   
       
   } ,
   "Tropies" : None
}
#########Here Sports,Country, Born are nested dictionary names in inside dictionary
print(inside) 
# to access the individual dictionary we have to use 2D array technique
print(inside["Country"]["Bangladesh"]) #Regular -> which is the value of Country dictionary Bangladesh keys 

#Now we also can create three dictionary first then add them to a new dictionay

Sports  = {
       "Cricket" : "international",
       "Football" : "Same"
   },
Country = {
       "Bangladesh": "Regular",
       "UK" : "NotRegular"
   },
Born = {
       "year":1975,
       "year1" : 1979   
       
   }

News = {                          #declare the dict names in string keys then , thats all
    "Sports" : Sports,
    "Country" : Country,
    "Born"    : Born
}

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(News)


dictu = {
    "inside": inside,                 #Here inside and myfamily both are a dictionary names
    "myfamily" : myfamily,
    "Sports" : Sports,                 #Sports,Country Born are also dictionary names
    "Country" : Country,
    "Born"  : Born           
}
print(dictu)


new =  {            #first have to change the dict names into a string "" then : then {} inside will be the keys at end a , 

   "Sports" :{
       "Cricket" : "international",
       "Football" : "Same"
   },
   "Country" : {
       "Bangladesh": "Regular",
       "UK" : "NotRegular"
   },
   "Born" : {
       "year":1975,
       "year1" : 1979   
       
   }
}
print(new)