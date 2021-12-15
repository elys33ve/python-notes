##### LISTS #####  

this = ['a','b','c','d','e','f']                          #list w strings
that = [1,2,3,4,5,6,7,8,9,10,11,12]                       #list w numbers
ok = [[1,2,3],[4,5,6],[7,8,9]]                            #list w columns

#access items
print(this[0])          #access item by position
print(this[-1])
print(this[:4])
print(this[1:4])

#modify lists
this[0] = 'x'           #change item by position
this.append('x')        #add to end of list
this.insert(2, 'x')     #insert at position
del this[3]             #delete
this.pop(2)             #pop ---> remove item from list but makes it accessable
this.remove('e')        #remove item by name
this.sort()             #sort by alphabetical/numberical order
this.reverse()          #reverse order

#other stuff
len(this)               #number items in list (len = "length" of list)
this_copy = this[:]     #copy list 
print(sorted(this))     #temporarily sort list (to print it)
print(''.join(this))    #join values into string

print(min(that))                        #min value in list (w numbers)
print(max(that))                        #max value in list (w numbers)
print(sum(that))                        #sum of list values (w numbers)

ok[1][2]                             #[row][column]
