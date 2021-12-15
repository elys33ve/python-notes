#another script of notes for file stuff

filename = "text.txt"                 #if same directory
filename = "C:\\files\text.txt"       #if not in same dir


def appFile (filename):               #add to end of file
    app = open(filename, 'a')
    a = input("append file: ")
    app.write(a)
    app.close()
    
def writeFile (filename):             #write over file
    w = input("write to file: ")
    write = open(filename, 'w')
    write.write(w)
    write.close()
    
def openFile (filename):              #open file and print lines
    read = open(filename, 'r')
    for x in read:
        print(x)
        
def readChar (filename):              #read specific # of characters
    read = open(filename, 'r')
    r = int(input("characters: "))
    print(read.read(r))
    read.close()
