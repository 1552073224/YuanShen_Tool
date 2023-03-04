#一个准备开启的小项目
#通过识别图像实现
import cv2
import numpy
import time

#code
tele_sign = cv2.imread('Images/teleportsign.png')
tele_ori = cv2.imread('Images/part.png')

ftime = time.time()
height,width,c =tele_sign.shape
result = cv2.matchTemplate(tele_sign,tele_ori,cv2.TM_CCOEFF_NORMED)
for y in range(len(result)):
    for x in range(len(result[y])):
        if result[y][x] > 0.99:
            cv2.rectangle(tele_ori,(x,y),(x + width,y + height),(0,0,255),2)
            print('Find!')


ltime = time.time()
print(f'{round(ltime - ftime,3)}s')
cv2.imshow('img',tele_ori)
cv2.waitKey()
cv2.destoryAllWindows()