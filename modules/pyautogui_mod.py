import pyautogui as p

#for (x,y) coordinates;
########x increases from left to right of screen
########y increases from top to bottom
########top left corner of screen is (0,0)

p.FAILSAFE = False      #disables failsafe that stops execution w cursor at corner of screen

x = 5       #x-coordinate
y = 500     #y-coordinate
c = 2       #clicks
i = 1       #interval (seconds)
b = 'left'  #button (left or right on mouse)
a = 100     #amount to scroll

p.position()            #current position of cursor on screen
p.onScreen(x,y)         #outputs whether the point exists on screen
p.size()                #screen resolution (height and width of screen)
p.moveTo(x,y)           #moves cursor to position
p.PAUSE = i             #pauses execution for given amt of time
p.moveRel(x,y)          #move relative to current position
p.click(x,y,c,i,b)      #mouse click
p.rightClick(x,y)       #right click
p.doubleClick(x,y)      #double click
p.tripleClick(x,y)      #triple click
p.middleClick(x,y)      #middle click
p.mouseDown(x,y,b)      #hold down 
p.mouseUp(x,y,b)        #release
p.scroll(a,x,y)         #scroll (+ a value for scroll up, - for down)
print(p.KEYBOARD_KEYS)  #prints the keys on keyboard
p.typewrite('text',i)   #types text (1 char at a time w i (s) between keystrokes)
p.hotkey('shift','x')   #press 2 keys simultaneously

ss = p.screenshot()                 #screenshot (ss would be the screenshot
p.screenshot(r'C:\path\ss.png')     #save screenshot to computer
p.screenshot(region=(0,0, x, y))    #screenshot specific region

p.confirm("continue")   #confirmation box pop-up
p.alert("oh no")        #alert box pop-up
p.prompt("question")    #prompt input pop-up

