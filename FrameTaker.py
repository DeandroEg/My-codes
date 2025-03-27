import cv2

frame2 = cv2.VideoCapture(r'C:\Users\User-name\Desktop\programing stuff\files for face detection\video frames taker\neg32.mp4')
tic = 4
frame_counter = tic
frame = 0

g=False
while g:
    succees, vid = frame2.read()
    cv2.imshow('it is just a txt', vid)
    gray_framed = cv2.cvtColor(vid , cv2.COLOR_BGR2GRAY)
    key = cv2.waitKey(1)
    if frame_counter == tic:
        frame_counter = 0
        gray_frame = cv2.resize(gray_framed, (100, 100))
        cv2.imwrite(r'C:\Users\User-name\Desktop\programing stuff\files for face detection\video frames taker\neg4\4frame' + str(frame) + '.jpg' , gray_framed)
    frame += 1    
    frame_counter += 1
    if key == 83 or key == 113:
        break


tic = 10
frame_counter = tic
frame = 0
area = 100
dd = True#False
while dd:
    succees, vid = frame2.read()
    cv2.imshow('it is just a txt', vid)
    gray_frame1 = cv2.cvtColor(vid , cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.resize(gray_frame1, (360, 640))
    key = cv2.waitKey(1)
    if frame_counter == tic:
        frame_counter = 0
        x, h= gray_frame.shape
        grids =0
        x1 =0
        x2=area
        y1=0
        y2=area
        ticerx =0
        xx= tryx=int(str(x/ area).split('.')[0])
        yy= tryy=int(str(h/ area).split('.')[0])
        done =False
        g = True
        if tryx == 0 or tryy == 0:
            print('no area')
            g = False
        while g:
            cv2.imwrite(r'C:\Users\User-name\Desktop\programing stuff\files for face detection\video frames taker\neg4\4frame' + str(frame)+'Split' + '.jpg' , gray_frame[x1:x2, y1:y2])
            grids +=1
            frame += 1  
            ticerx+=1
            if ticerx != xx:
                x1 += area
                x2 += area

            else:
                ticerx = 0
                if x-area*xx >= 15:
                    cv2.imwrite(r'C:\Users\User-name\Desktop\programing stuff\files for face detection\video frames taker\neg4\4frame' + str(frame)+'Split' + '.jpg' , gray_frame[x-area:x, y1:y2])
                    grids +=1
                y1 += area
                y2 += area
                x1 = 0
                x2 = area
                tryy-=1

            if tryy == 0:
                if h-area*yy < 15 or  done:
                    print(grids)
                    g = False
                else:
                    y1 =h-area
                    y2 =h
                    tryy +=1
                    done = True

    frame_counter += 1
    if key == 83 or key == 113:
        break



grids =0
x1 =0
x2=area
y1=0
y2=area
ticerx =0
xx= tryx=int(str(x/ area).split('.')[0])
yy= tryy=int(str(h/ area).split('.')[0])
done =False
g = False#True
if tryx == 0 or tryy == 0:
    print('no area')
    g = False
while g:
    cv2.imwrite(r'C:\Users\User-name\Desktop\programing stuff\files for face detection\video frames taker\neg3\3frame' + str(frame)+'Split' + '.jpg' , gray_frame[x1:x2, y1:y2])
    grids +=1
    frame += 1  
    ticerx+=1
    if ticerx != xx:
        x1 += area
        x2 += area

    else:
        ticerx = 0
        if x-area*xx >= 15:
            cv2.imwrite(r'C:\Users\User-name\Desktop\programing stuff\files for face detection\video frames taker\neg3\3frame' + str(frame)+'Split' + '.jpg' , gray_frame[x-area:x, y1:y2])
            grids +=1
        y1 += area
        y2 += area
        x1 = 0
        x2 = area
        tryy-=1

    if tryy == 0:
        if h-area*yy < 15 or  done:
            print(grids)
            g = False
        else:
            y1 =h-area
            y2 =h
            tryy +=1
            done = True