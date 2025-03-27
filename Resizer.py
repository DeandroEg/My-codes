import cv2
import os
frame = 0

for file_type in ['100pananas']:
    for name in os.listdir(file_type):
        print(name)
        im = cv2.imread(r'C:\Users\User-name\Desktop\programing stuff\files for face detection\video frames taker\100pananas'+'\\'+name)
        h0, w0 ,j= im.shape
        if h0 > w0:
            hw = (h0/100)
        else:
            hw = (w0/100) 
        h = int(str(h0/ hw).split('.'))
        w = int(str(h0/ hw).split('.'))
        redoh = 0
        redow = 0
        if list(h[1])[0] >= 5 :
            if list(h[1])[1] >= 5:
                redoh =1
            elif list(h[1])[0] >= 6 :
                redoh =1
        elif list(w[1])[0] >= 5:
            if list(w[1])[1] >= 5:
                redow =1
            elif list(w[1])[0] >= 6 :
                redow =1
        image0 = cv2.resize(im, (w[0]+redow, h[0]+redoh))
        image = cv2.cvtColor(image0 , cv2.COLOR_BGR2GRAY)
        frame += 1
        exs1 = str(name).split('.')
        exs = '.' + str(exs1[-1])
        cv2.imwrite(r'C:\Users\User-name\Desktop\programing stuff\files for face detection\video frames taker\100pananas\panana' + str(frame) + exs , image)
