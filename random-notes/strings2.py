#more notes for strings and variables

print("hi")               #print string
print('hi')               #string works w 'this' or "this"
print("hi'hi'hi")         #can use "these" inside 'these' or vise versa
print('hi"hi"hi')

hi = "aaaaaaaaaaaaa"          #variable w string -------> (letters,numbers,underscores work as variable names, cant start w number tho)
eee = "7777"                  #also variable w string (bc in "")
rere = 555555                 #variable w integer
print(rere)

thing = "this is a thing"                         #title() makes first letters uppercase
thing1 = "oh shit aaaaaa"                         #upper() makes all string letters uppercase
thing2 = "asdfjla;ksdjf"                          #lower() makes all string letters lowercase
print(thing.title())
print(thing1.upper())
print(thing2.lower())

string1 = "this is stuff"                       #formating strings w variables idk
string2 = "ooh thecurly brackets fancy"                 
both = f"{string1} {string2}"                   #the f means format i think
print(both)       

whitespacer = "thsadfjkl  "       #whitespace = extra space in string. "hi " and "hi" r technically different strings
whitespacer.rstrip()              #rstrip() strips the extra space from the right of a string (helpful when comparing strings)
whitespacel = " jdjdjdj"
whitespacel.lstrip()              #lstrip() removes whitespace from left of string
whitespace = " hi "
whitespace.strip()                #strip() removes whitespace from l and r

whitespace = whitespace.strip() #this also works, just does it for variable automatically/permanently

a, b, c = 1, 2, 3   #initialize multiple variables in one line (good for shortening programs)
CONSTANT = 400      #no built in constant type but ppl use all uppercase to indicate value that shouldn't be changed  
