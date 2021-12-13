#### Lists:     lists are just variables that have multiple values                                        
this = ['a','b','c','d','e','f']                          #list w strings
that = [1,2,3,4,5,6,7,8,9,10,11,12]                       #list w numbers
these = [[1,2,3],[4,5,6],[7,8,9]]                         #list w columns

this[0] = 'aa'          #replace ------> set up like: *list name*[*position in list*] = *replacement value* ----> (so in this case 'a' would become 'aa' becase 'a' is at position 0)
this.append('g')        #add to end of list
this.insert(2, 'cc')    #insert @ position
del this[3]             #delete
this.pop(2)             #pop ---> takes item out of list but makes it accessable
this.remove('e')        #remove item by name
this.sort()             #sort by alphabetical/numberical order
this.reverse()          #reverse order
len(this)               #number items in list (len = "length" of list)
print(this[1:4])        #'range' of list items
print(this[:4])         #0 to end range
print(this[-3:])        #last items ---> if you use a negative number for position in list, it goes backwards
this_copy = this[:]     #copy list 
print(sorted(this))     #temporarily sort list (to print it)

print(min(that))                        #min value in list (w numbers)
print(max(that))                        #max value in list (w numbers)
print(sum(that))                        #sum of list values (w numbers)

these[1][2]                             #[row][column]
