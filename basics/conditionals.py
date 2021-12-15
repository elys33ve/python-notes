#### Conditionals:
x = 1 
y = 2 
z = 3

#if, elif, else
                    #ex. 1
if x < y:                              #if statement
  print("x is less than y")                #executes if (x<y in this case) is TRUE
elif x > y:                            #elif statement ("else if")
  print("x is greater than y")             #executes if the if statement is FALSE but elif is TRUE
elif x == y:                           #(u can have many elifs)
  print("x is equal to y")
else:                                  #else statement
  print("huh?")                            #executes if all of the elif or if statements are FALSE 

                    #ex. 2
if x + y == z:
  print("x plus y equals z")
  if x and y == 1 or 2:                  #nested if statement
    print("x is:",x,"and y is:",y)          #executes if the nested if is TRUE and the first is also TRUE
    print("so",x,"plus",y,"equals",z)
