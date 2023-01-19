 #Dictionary contain a key and an element
 #It used curly braces like tuples and list
 #{}
 #Dictionary contain more than one datatypes
#They are indexed
#Are changeable
#Doesnt allow duplication

Laptop ={
    "Type":"Hp",
    "Book":"EliteBook",
    "RAM":"8.00GB",
    "Speed":"2.56Ghz",
    "Processor":"64-bit",
    "Device Name":"Samantha"
}
print(Laptop)

#Updating a dictionary
#You refer to the key instead of the index

Laptop.update({"Device Name":"Coding"})
print(Laptop)

#Removing elements from a dictionary
#Laptop.pop("Device Name")
print(Laptop)

#Deleting elements in dictionary
#del Laptop["Device Name"]
print (Laptop)

#Combining several dictionaries
#Making one dictionary out of many dictionaries
Finance ={
    "Cost":"30,000",
    "Buyer":"Myself"
}
Laptop.update(Finance)
print(Laptop)