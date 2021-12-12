#### Reading/Writing to Files:
filename = "text.txt"                 #if same directory
filename = "C:\\files\text.txt"       #if not in same dir (add path)

read = open(filename, 'r')            #read file
app = open(filename, 'a')             #append/add to file
write = open(filename, 'w')           #write/write over file
rewr = open(filename, 'w+')           #read and write file

print(read.read(10))                  #read (# of characters)
app.write("stuff")                    #append (string of stuff)
write.write("stuff")                  #write (string of stuff)
read.close()                          #close file

for x in read:                        #prints line by line
  print(x)
