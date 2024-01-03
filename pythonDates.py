"""
Python Dates

"""

#Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
"""
The strftime() Method
The datetime object has a method for formatting date objects into readable strings.
"""
print(x.strftime("%d")) # to print only the days
print(x.strftime("%m")) # month
print(x.strftime("%A"))#to find the recent day name
print(x.strftime("%B"))#to find the recent month name



#The datetime() class requires three parameters to create a date: year, month, day.

x = datetime.datetime(2023, 9, 21, 12, 45, 50, 30)

print(x)  #2023-09-21 12:45:50.000030
