import cv2
from random import randrange

traind_face_harr = cv2.CascadeClassifier(r'C:\Users\User-name\Desktop\programing stuff\files for face detection\files2 for face haar\panana2-cascade-10st.xml')
smile_harr = cv2.CascadeClassifier(r'C:\Users\User-name\Desktop\programing stuff\files for face detection\files2 for face haar\haarcascade_smile.xml')

#choose
work = True
while work:
    answer = ("3")#str(input("chosse bettwen 1 for image and 2 for video or 3 for camera : "))
    if answer == ("1"): 
        work = False
    elif answer == ("2"): 
        work = False
    elif answer == ("3"):
        work = False
    else :
        print("wrong answer")

#image
if answer == ("1"):
    image = (r'C:\Users\User-name\Desktop\programing stuff\files for face detection\video frames taker\images\frame875.jpg')#input("enter image name : ") + (".png")
    frame2 = cv2.imread(image)
#video
elif answer == ("2"):
    video = ((r'C:\Users\User-name\Desktop\programing stuff\files for face detection\video frames taker\20240806_131924.mp4'))#input("enter video name : ") + (".mp4")
    frame = cv2.VideoCapture(video)
#camera
elif answer == ("3"):
    frame = cv2.VideoCapture(0)

while True:
    if answer != ("1"):
       succees, frame2 = frame.read()
       #frame2 = cv2.resize(frame2 , (800, 800))
    #to work on it
    gray_frame = cv2.cvtColor(frame2 , cv2.COLOR_BGR2GRAY)
    #face location
    face_place = traind_face_harr.detectMultiScale(gray_frame, 15,15)

    #draw
    for (a, b, c, d) in face_place:
       # if c >= 40:
        #    if d >= 40:
        cv2.rectangle(frame2, (a,b), (a+c, b+c), (randrange(128,256), randrange(128,256), randrange(128,256), 5))
    cv2.imshow('it is just a txt', frame2)
    if answer == ("1"):
        cv2.waitKey()
        break
    else :
        key = cv2.waitKey(1)
        if key == 83 or key == 113:
            break
if answer == ("3"):
    frame.release()      
print("done")