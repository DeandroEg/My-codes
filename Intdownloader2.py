import pyautogui
import keyboard
num = 0
x1 = 0
y1 = 0
#pyautogui.moveTo(,)
#pyautogui.scroll(-100)#,116,115)
#g = False#True
g = True
while g:
    #input('enter tries: ')pppqpq
    if keyboard.is_pressed('p') or keyboard.is_pressed('P'):
        x , y=pyautogui.position()
        if x1 != x and y1 != y:
            num+= 1
            print(str(num)+' ' + str(x),str(y))
            open('program.txt', 'a').write('pyautogui.leftClick('+str(x)+','+str(y)+')'+'\n')
        x1 =x
        y1 =y
    elif keyboard.is_pressed('m') or keyboard.is_pressed('M'):
        open('program.txt', 'a').write('#a mark'+'\n')
    elif keyboard.is_pressed('q') or keyboard.is_pressed('Q'):
        break