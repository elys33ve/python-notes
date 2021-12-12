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

#### Basic Outputs:                        usually, if you want something to be an output, u will use the print() method.
x = 3
y = 3.2
z = 'string'

print("hi")                                 #u can put strings directly in the print() function
print(x)                                    #or variables that have been defined 
print(23)                                   #or numbers
print(235-23+2)                             #or equations (and itll print the answer)

#formatting
print("stuff {0:.4f}".format(x))                                    #4 decemal places      (u need the 'f' for some reason if ur doing this)
print("stuff {0:.9f}".format(y))                                    #9 decemals
print("stuff {0}".format(x))                                        #integers work w this method
print("stuff {0}".format(z))                                        #string 
print("stuff {0}, more stuff {1}, moooore {2}".format(x,y,z))       #mix (the numbers inside the {} just specify the order, so x is 0, y is 1, z is 2.)
