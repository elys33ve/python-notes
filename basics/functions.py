##### FUNCTIONS #####
x = 1
y = 2
z = 3

#function
def this():           #defining a function (parameters/arguments in parenthesis)
  global z                      #use global to modify a global variable from inside function
  global x
  x = x * y                     #what the function does
  z = z * y                            
  return x, z                   #use 'return' to tell it what to output/where to go next

this()                #calling the function
