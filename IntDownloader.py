import os
import cv2
import pytesseract
import pyautogui
import keyboard
import time
num= 100

def ahally(confi):
    while True:
        try:
            l, t, w, h = pyautogui.locateOnScreen('recoFiles\\nicest33.png',region=(int(702),int(350),int(468),int(417)), confidence=confi)
            pyautogui.screenshot('screen3.png',region=(int(l), int(t), int(w), int(h)))
            path = r'C:\Users\User-name\Desktop\programing stuff\python libriries and needed programs\Tesseract-OCR\tesseract.exe'
            pytesseract.pytesseract.tesseract_cmd = path
            grayImage = cv2.cvtColor(cv2.imread('screen3.png'), cv2.COLOR_BGR2GRAY)
            (_, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY_INV)
            num1 = str(pytesseract.image_to_string(blackAndWhiteImage, config="--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789x)"))
            num = num1.split(')')[1].replace('\n','').split('x')
            if len(num[0]) == 6:
                num = [list(num)[0,1,2],list(num)[3,4,5]]
            elif len(num[0]) == 5:
                num = [list(num)[0,1,2],list(num)[3,4]]
            pyautogui.doubleClick(488, 354)
            pyautogui.typewrite(num[0])
            pyautogui.doubleClick(590, 360)
            pyautogui.typewrite(num[1])
            #pyautogui.doubleClick(695, 347)
            os.remove('screen3.png')
            break
        except pyautogui.ImageNotFoundException:
            break

def workOfmain(image,twicer):
    button7location2 = pyautogui.locateOnScreen(image, confidence=0.9)
    mx1 , my1= pyautogui.center(button7location2)
    pyautogui.click(mx1 , my1)
    if twicer == 1:
        pyautogui.click(mx1 , my1)

def detectMian(image, once, twicer):
    while True:
        try:
            workOfmain(image,twicer)
            break
        except pyautogui.ImageNotFoundException:
            print('n')
            if once == True:
                break

def detector2(twicerkey):
            pyautogui.hotkey("ctrl", "c")
            pyautogui.hotkey("ctrl", "n")
            ahally(confi=0.6)

            detectMian('recoFiles\\button6.png', once = False, twicer=2)
            time.sleep(.51)
            #detectMian('recoFiles\\button5.png', once=True, twicer=2)

            pyautogui.hotkey("ctrl", "v")
            pyautogui.hotkey("ctrl", "s")

            detectMian('recoFiles\\button3.png', once = False, twicer=2)
            detectMian('recoFiles\\button4.png', once = False,twicer=  twicerkey)

while True:
    if keyboard.is_pressed('x') or keyboard.is_pressed('X'):
        pyautogui.rightClick()
        detectMian('recoFiles\\button1.png', once = False, twicer=2)
        detectMian('recoFiles\\button2.png', once = False, twicer=2)
        num+=1
        print("d x"+ str(num))
            
    elif keyboard.is_pressed('g') or keyboard.is_pressed('G') :
        detector2(twicerkey = 2)
    elif keyboard.is_pressed('f') or keyboard.is_pressed('F'):
        detector2(twicerkey = 1)
    elif keyboard.is_pressed('q') or keyboard.is_pressed('Q'):
        print("d x"+ str(num))
        break
    