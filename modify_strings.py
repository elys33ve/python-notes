#### Modifying Strings & String Shit:       
#Examples:    
this = "hello world"               
that = "hi {}, hello {}."
ooo = ":/"
pi = 3.1415926535

print(that.format(this,ooo))                               #format --> add things/combine
print("pi to 5 decimal places is {0:.5f}".format(pi))      #format --> when combining floats: {*placement*:.*number of decimal places*f}

print(this.upper())             #all uppercase
print(this.lower())             #all lowercase
print(this.title())             #first letter of words uppercase
print(this.strip())             #strips extra spaces form front and back
print(this.replace("l","e"))    #replace
print(this.split(","))          #split ----> ["hello","world"]

print("hi\nhi")                 #new line --> \n
print("a\bhi")                  #backspace --> \b
print("\thi")                   #tab --> \t
