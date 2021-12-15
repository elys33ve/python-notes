##### STRINGS #####                                                     (plus some formatting integers)     

this = "hello world"               
that = "hi {}, hello {}."
what = "abcdefghijklmnopqrstuvwxyz"
shit = "123456789"
fuck = "  fuuuck  "
pi = 3.1415926535

#formatting
print("x: {0}, y: {1}, z: {2}".format(x,y,z))              #format --> (the numbers inside the {} just specify the order, so x is 0, y is 1, z is 2.)
print(that.format(this,what))                              #combine shit
print("pi to 5 decimal places is {0:.5f}".format(pi))      #integers --> when combining floats: {*placement*:.*number of decimal places*f}
print("*stuff* {0}".format(this))                          #strings
print(f"aaaaaaaa, {this}")                                 #the better way to format

#slicing strings
print(what[5])                  #character @ position 5 (f)
print(shit[1:5])                #2345
print(this[6])                  #spaces count
print(shit[:])                  #all
print(this[:5])                 #everything before 5
print(this[5:])                 #everything after 5
print(that[7:12])               #characters from position 7 to 12
print(what[-1] )                #last position
print(that[-10:-4])             #after 10th last to 4th last

#modify strings
print(this.upper())             #all uppercase
print(this.lower())             #all lowercase
print(this.title())             #first letter of words uppercase
print(this.strip())             #strips whitespace
print(fuck.rstrip())            #strips whitespace from end
print(fuck.lstrip())            #strips whitespace from beginning
print(this.replace("l","e"))    #replace --> (replace first string with second string in original)
print(this.split(","))          #split ----> ["hello","world"]

print(shit + what)              #add strings
print(shit + ' ' + what)        #add strings with space

#other string methods
print(this.find('h'))           #returns position of value (returns -1 if not found)
print(this.index('h'))          #returns position of value
print(what.isalnum())           #returns true if all characters are alphanumeric
print(shit.isdigit())           #true if all are numbers
print(shit.isidentifier())      #true if identifier
print(what.islower())           #true if all are lowercase
print(shit.isnumeric())         #true if all are numeric
print(what.isprintable())       #true if string is printable
print(fuck.isspace())           #true if all characters are whitespace
print(this.istitle())           #true if all words are capitalized
print(this.isupper())           #trie if all characters uppercase
print(what.isalpha())           #returns true if all characters are in alphabet (so spaces excluded)
print(what.isdecimal())         #returns true if all characters are decimal
print(this.capitalize())        #capitalize first word
print(this.count('l'))          #count # of times value appears in string
print(str.encode(this))         #encodes string --> (converts to bytes)
print(this.endswith('world'))   #returns true if it ends w value
print(this.startswith('h'))     #true if starts with value
print(this.splitlines())        #splits string at newline
print(this.swapcase())          #swaps case of letters

#escape characters
print('\'')           #single quote
print('\\')           #backslash
print('\n')           #newline
print('\r')           #carriage return
print('\t')           #tab
print('\b')           #backspace
print('\f')           #form feed
print('\ooo')         #octal value
print('\xhh')         #hex value
