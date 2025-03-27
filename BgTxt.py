import os
import cv2
import io

neg = r'C:\Users\User-name\Desktop\programing stuff\files for face detection\video frames taker\neg'
for file_type in [neg]:
    for img in os.listdir(file_type):
        if file_type == neg:
            line = 'neg'+ '/' + img  + '\n'
            with io.open('bg2.txt', 'a', newline='\n') as f:
                f.write(line)

#for file_type in ['neg']:
 #   for img in os.listdir(file_type):
  #      if file_type == 'neg':
   #         img2 = (r'C:\Users\User-name\Desktop\files for face detection\video frames taker\neg' + '/'+str(img))
    #        frame = cv2.imread(img2)
     #       mig = cv2.resize(frame, (100, 100))
       #     cv2.imwrite(r'C:\Users\User-name\Desktop\files for face detection\video frames taker\neg' + '/'+str(img), mig)
