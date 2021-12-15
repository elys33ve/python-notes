##### LOOPS #####                        

#for loops --> (for iterate specific # of times)
List = ['a','b','c','d','e','f'] #list name can be any variable btw

for i in range(0,5):        #for loop w range              
  print("hi")                   #executes for each value in range
print(i)                    #iterations (doesnt have to b 'i' just whatever variable u have in that position)

for List in List:           #for loop w list 
  print(List)                   #executes each item in list
 

#while loops --> (# of iterations determined by if condition is met)
T = True
x = 1

while T == True:          #while loop                                                   ---> set up like:       while *condition*:
  x = x + 8                   #performs as long as condition True
  if x > 100:
    print(x)          
    T = False                 #makes condition False, stops while loop when if condition me
  elif x > 200:
    break                     #break will break loop
  else:
    pass

  
