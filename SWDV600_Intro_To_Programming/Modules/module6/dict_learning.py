"""
All about Python Dictionaries

\n

OPERATORS:
for <key> in <dict> = iterates through all of the keys in the dictionary

METHODS:
in => searches the dictionary, returns boolean :: <item> in <dict>
del => removes <item> from dictionary :: del <dict>[<key>]
keys => returns the keys of the dictionary :: list( <dict>.keys() )
values => returns the values of the dictionary :: list( <dict>.keys() )
get => gets the passed in key (first arg) of the dictionary, second arg is
\tdefault value if the first arg is not in the dictionary :: <dict>.get(<key>, <default value>)

"""

carSales = {'red': 8, 'blue': 2, 'green': 5, 'silver': 6 }
totalSales = 0
for carSalesKey in carSales:
    totalSales += carSales[carSalesKey]

print(totalSales)