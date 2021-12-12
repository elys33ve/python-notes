#### Data Types:    

#Examples:                     
x = "hi"                                       #str --> string = anything in parenthases (either 'one' or "two" work)
x = 20                                         #int --> integer = any + or - whole number
x = 10.01                                      #float --> decimal number
x = 1j                                         #complex --> (ex: 28e9, 2.938E-3, then like; pi, imaginary #'s, irrational numbers, etc.)
x = ['a','b','c']                              #list --> collection of values
x = True                                       #bool --> boolean: True or False
x = range(5)                                   #range --> starts at 0 (unless u specifiy like in range(1,8)) example: range(5) is 5 values, but the values would be 0,1,2,3,4 and not include 5)
x = ('a','b','c')                              #tuple --> similar to a list but worse
x = {"name" : "me", "age" : 293}               #dict --> dictionary: {key:value} order, assigns each value to a "key" within the dictionary value
x = {"this","that","these"}                    #set --> another thing similar to a list
x = frozenset({"this","that","these"})         #frozenset --> a set that can't be modified
x = b"hello"                                   #bytes
x = bytearray(5)                               #bytearray
x = memoryview(bytes(5))                       #memoryview

print(type(x))                                 #show type


#### Casting: converting a certain data type to a different data type
x = str(324)          #convert to string --> '342'
x = float("34")         #convert to float --> 34.0
x = int(534.623)     #convert to integer --> 534
