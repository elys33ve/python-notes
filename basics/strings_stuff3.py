this = ['this', 'is', 'a', 'list']      #thats a list.
print(this)                             #prints the list in list form
print(this[0])                          #prints particular thing on list (0 is first thing)
print(this[1].title())                  #works like normal string w shit
print(this[-1])                         #-1 prints last thing in list (useful if u want last thing but dont know what it is/how many in list)


this = ['xxx','bbb','ccc']      
this[0] = 'aaa'                 #replace element in list
this.append('ddd')              #add element to end of list
this.insert(2, 'xxx')           #insert element ---> (position, element)
del this[0]                     #delete element 
pop = this.pop(0)               #takes out element from list but still exists/accessable
this.remove('ccc')              #remove item by value
print(this)
print(pop)

empty_list = []                 #can also start w empty list and just add shit
empty_list.append('hi')
print(empty_list)


this = ['d','s','j','a','e']
that = [2,4,6,34,6865,3,64]
this.sort()                       #permanently sort (by alphabetical order)
that.sort()                       #(or by numerical order)
this.sort(reverse=True)           #reverse alphabetical
that.sort(reverse=True)           #reverse numerical
print(this)
print(that)


this = ['d','s','j','a','e']
print(sorted(this))             #temporarily sort list
this.reverse()                  #reverses order           (permanent but can change back by reverse() again)
print(this)


this = ['d','s','j','a','e']
len(this)                           #length of list (by how many items in it)


this = ['aaa','ddd','eee','www','ooo']
for this in this:                           #basically "for every item in 'this':" but ye
  print(this)
  
  
for value in range(1,6):        #will print each value in the range (starting at the first, stopping when reaches the last)
  print(value)
  
  
  numbers = list(range(0,6))            #turns range into list of #s in the range
print(numbers)

even_numbers = list(range(2,11,2))    #even #s in range ---> range(first #, last #, count by)
print(even_numbers)

squares = []
for value in range (1,6):             #for each value in range: square it, add to list, print list
  square = value**2
  squares.append(square)
print(squares)

squares = [value**2 for value in range(1,6)]        #another way to do the sqaure #s in list for loop
print(squares)


number = [1,2,3,4,5,6,7,8,9,10,11,12]
print(min(number))                        #min in list
print(max(number))                        #max in list
print(sum(number))                        #sum of list values


this = ['aaa','ddd','eee','www','ooo']
print(this[1:4])                          #'range' of list items (same as range, starts at [1], stops when reaches [4])
print(this[:4])                           #same but blank before/after : just means start from beginning/stop at end
print(this[-3:])                          #indicates last 3 items on list

that = this[:]                            #make copy of list for another variable
print("og list: ", this)
print("copied list: ", that)


this = (222,55)       #tuple (similar to list)
print(this[0])
print(this[1])
thiss = (3,)          #tuples need comma (w one element, still has comma)


this = (333,444,555)      #loop w tuple
for this in this:
  print(this)
  
  
this = (111,222,333)
print(this)
this = (1,2,3)            #instead of modifying like lists, u can write over tuples
print(this)
